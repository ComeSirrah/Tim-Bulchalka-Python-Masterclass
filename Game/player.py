class Player(object):

    def __init__(self, name):
        self.__name = name
        self.__lives = 3
        self.__level = 1
        self.__score = 0

    @property
    def name(self):
        return self.__name

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, lives):
        if lives >= 0:
            self.__lives = lives
        else:
            print("lives cannot be negative")
            self.__lives = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        if level >0:
            delta = level - self.__level
            self.__score += delta * 1000
            self.__level = level
        else:
            self.__level = 1
            self.__score = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    def __str__(self):
        return f"Name:{self.name} | Lives: {self.lives} | Level: {self.level} | Score: {self.score}"
