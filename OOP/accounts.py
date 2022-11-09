import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        print("Account created for " + self._name)
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), balance))

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("insufficient funds for withdrawal")
            self.show_balance()

    def show_balance(self):
        print(f"the current balance of {self._name} is {self._balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount} {tran_type} on {date}, ({date.astimezone()} local time)")


if __name__ == '__main__':
    sirrah = Account('sirrah', 0)
    sirrah.show_balance()

    sirrah.deposit(1000)
    sirrah.withdraw(500)
    sirrah.withdraw(700)
    sirrah.withdraw(49)
    sirrah.show_transactions()

    print(f"\n\n\n\n")

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
