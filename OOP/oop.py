class Kettle(object):

    power_source = "electricity"
    def __init__(self, make, price):
        self.make = make
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

print(Kettle.power_source)
print(kenwood.power_source)
print(zojirushi.power_source)