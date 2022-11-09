class Kettle(object):

    power_source = "electricity"    # a class attribute

    def __init__(self, make, price):
        self.make = make            # an instance attribute
        self.price = price
        self.on = False

    def switch(self):
        if not self.on:
            self.on = True
        else:
            self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

zojirushi = Kettle("Zojirushi", 18.99)

print(f"Models: {kenwood.make} = {kenwood.price}, {zojirushi.make} = {zojirushi.price}")

print(zojirushi.on)
zojirushi.switch()
print(zojirushi.on)
zojirushi.switch()
print(zojirushi.on)

print("*" * 80)

print()
kenwood.power = 1.5
print(kenwood.power)

print("Switching to atomic power")
Kettle.power_source = "Nuclear Reactor - Fissile"
print(Kettle.power_source)
print("switching kenwood to gas")
kenwood.power_source = 'gas'
print(kenwood.power_source)
print(zojirushi.power_source)
print(Kettle.__dict__)
print(zojirushi.__dict__)
print(kenwood.__dict__)
