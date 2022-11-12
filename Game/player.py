class Player(object):

    @property
    def lives(self):
        return self._lives

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    @lives.setter
    def lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("you died")
            self.lives = 0

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Level: {self.level}, Score: {self.score}"
