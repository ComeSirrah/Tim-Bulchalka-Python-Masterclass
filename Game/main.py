from enemy import Enemy, Troll, Vampire


ugly_troll = Troll("Ug")
uglier_troll = Troll("Urg")
ugliest_troll = Troll("Ulg")
vampire_1 = Vampire("Radluca")
Vampire_2 = Vampire("Edward")

while vampire_1.alive:
    vampire_1.take_damage(1)
    print(vampire_1)
