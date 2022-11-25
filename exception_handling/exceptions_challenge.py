def simple_division(a: int, b: int) -> float:
    """
    :param a: number to be divided
    :param b: number to divide by
    :return:  the quotient of a / b
    """
    pass
    if a == 0:
        return 0
    else:
        try:
            return a / b
        except ZeroDivisionError:
            print("Uh, you can't divide by zero, bud.")
            return "Maybe take a math class?"


print(simple_division(10, -0))
