class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee! This is fun!")
        elif self.ratio == 1:
            print("Hard work... but I'm flying.")
        else:
            print("I think i'll just walk.")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("waddle waddle waddle")

    def swim(self):
        print("splish splash")

    def quack(self):
        print("quack quack")

    def fly(self):
        self._wing.fly()


class Mallard(Duck):
    pass


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("waddle waddle waddle, I can waddle too.")

    def swim(self):
        print("splish splash. Brrr.")

    def quack(self):
        print("Uh... I'm a penguin.")

    def aviate(self):
        print("I won the lottery and bought a learjet.")


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, *ducks: Duck) -> None:
        for duck in ducks:
            fly_method = getattr(duck, "fly", None)
            if callable(fly_method):
                self.flock.append(duck)
            else:
                raise TypeError(f"Cannot add duck, are you sure it's not a {str(type(duck).__name__)}?")

    def migrate(self):
        error = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("An attribute error has occurred")
                error = e
        if error:
            raise error


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
