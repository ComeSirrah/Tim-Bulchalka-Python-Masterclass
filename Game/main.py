from player import Player

david = Player("Sirrah")

print(david)
david.lives -= 1
print(david)
david.lives -= 4
print(david)


david._lives = 9
print(david)

