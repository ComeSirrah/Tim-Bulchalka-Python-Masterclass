def spam_1():

    def spam_2():

        def spam_3():
            z = " and even"
            z += y.removesuffix(",")
            z += "."

            # print(f"In spam_3, locals are {locals()}")
            return z

        y = " more "    # y must exist before spam_3 is called.
        y += x          # do not combine these assignments.
        y += spam_3()
        # print(f"In spam_2, locals are {locals()}")
        return y

    x = "spam,"         # x must exist before spam_2 is called.
    x += spam_2()        # do not combine these assignments.
    # print(f"In spam_1, locals are {locals()}")
    return x


print(spam_1())

print('\n \n \n')

print('Locals:')
state = locals().copy
for l in state():
    print(l)

print('\n \n \n')

world = globals().copy()
print("Globals:")
for g in world:
    print(g)