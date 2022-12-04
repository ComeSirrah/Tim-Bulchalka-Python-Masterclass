import ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Mallard()
percy = ducks.Penguin()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()


flock.add_duck(donald, daisy, duck3, duck4, percy, duck5, duck6, duck7)

flock.migrate()