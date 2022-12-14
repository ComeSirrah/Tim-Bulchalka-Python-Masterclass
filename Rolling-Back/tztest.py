import datetime
import sqlite3
import pytz
import pickle

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, zone INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') "
           "AS localtime, history.account, history.amount FROM history ORDER BY history.time")


class Account(object):

    @staticmethod   # static methods are used when the method/function does not access any properties
    # of a class, but it still makes logical sense to have it belong to the class. These are generally
    # utility functions to be used when doing other things with the class and its objects.
    def _current_time():
        # return pytz.utc.localize(datetime.datetime.utcnow())
        utc_time =  pytz.utc.localize(datetime.datetime.utcnow())
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo
        return utc_time, zone

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name =?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print(f"retrieved record for {self.name}.", end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print(f"account created for {self.name}.", end="")
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time, zone = Account._current_time()
        pickled_zone = pickle.dumps(zone)
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES(?, ?, ?, ?)", (deposit_time, self.name, amount, pickled_zone))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print(f"{amount / 100:.2f} deposited into account:\t{self.name}")
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if self._balance >= amount > 0:
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdrawal_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
            print(f"{amount / 100:.2f} withdrawn from account:\t{self.name}")
            return amount / 100
        else:
            print("The amount must be greater than zero, but no more than your account balance.")
            return 0.0

    def show_balance(self):
        print(f"Balance on account {self.name}:\t{self._balance/100:.2f}")


if __name__ == '__main__':

    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("Terry")
    graham = Account("Graham", 9000)
    eric = Account("eric", 7000)
    michael = Account("Michael")
    terryG = Account("TerryG")

    db.close()
