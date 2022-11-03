def spam_1():

    def spam_2():

        def spam_3():
            z = " even more spam"
            print(f"In spam_3, locals are {locals()}")
            return z


        y = " more spam"
        y += spam_3()
        print(f"In spam_2, locals are {locals()}")
        return y

    x = "spam"
    x += spam_2()
    print(f"In spam_1, locals are {locals()}")
    return x


print(spam_1())
