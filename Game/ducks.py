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

class Penguin(object):

    def __init__(self):
        pass

    def walk(self):
        print("waddle waddle waddle, I can waddle too.")

    def swim(self):
        print("splish splash. Brrr.")

    def quack(self):
        print("Uh... I'm a penguin.")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly()

    # percy = Penguin()
    # test_duck(percy)
