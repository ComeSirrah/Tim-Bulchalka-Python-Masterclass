import math
import random


class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True
        self.base_hp = hit_points
        self.res_increment = 1

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points > 0:
            self.hit_points = remaining_points
            print(f"{self.name} took {damage} hit point(s) of damage")
        else:
            self.hit_points = 0
            if self.lives > 1:
                self.lives -= 1
                print(f"{self.name} has flouted death.")
                self.hit_points = math.ceil(self.base_hp - ((self.base_hp * 0.3) * self.res_increment))
                self.res_increment += 1
            else:
                self.lives = 0
                self.alive = False
                print(f"{self.name} has been defeated")

    def __str__(self):
        return f"Name: {self.name} | Lives: {self.lives} | Hit Points: {self.hit_points}"


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1, 9) == 9:
            print(f"{self.name} dodged the attack!")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print(f"Me {self.name}. {self.name} stomp you!")

