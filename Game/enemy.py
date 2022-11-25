import math
import random


class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True
        self._base_hp = hit_points
        self._res_increment = 1

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points > 0:
            self._hit_points = remaining_points
            print(f"{self._name} took {damage} hit point(s) of damage")
        else:
            self._hit_points = 0
            if self._lives > 1:
                self._lives -= 1
                print(f"{self._name} has flouted death.")
                self._hit_points = math.ceil(self._base_hp - ((self._base_hp * 0.3) * self._res_increment))
                self._res_increment += 1
            else:
                self._lives = 0
                self._alive = False
                print(f"{self._name} has been defeated")

    def __str__(self):
        return f"Name: {self._name} | Lives: {self._lives} | Hit Points: {self._hit_points}"


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1, 7) == 7:
            print(f"{self._name} dodged the attack!")
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
        print(f"Me {self._name}. {self._name} stomp you!")


class VampireDaywalker(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140
        self._lives = 1


    def take_damage(self, damage):
        if damage < 4:
            super().take_damage(1)
        else:
            super().take_damage(damage//4)


