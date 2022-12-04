import sys



def _git_int():
    """
    :return: (a, b)
    """
    while True:
        try:
            a = input("What's the numerator?\n")
            b = input("And the denominator?\n")
        except EOFError:
            sys.exit(0)
        finally:
            print("The finally clause always executes")

        try:
            return float(a), float(b)
        except ValueError:
            print("Each input needs to be a valid int or a float.")


def simple_division() -> float:
    """
    :return:  the quotient of a / b
    """

    a, b = _git_int()

    if a == 0:
        return 0
    else:
        try:
            answer = a / b
        except ZeroDivisionError:
            print("Uh, you can't divide by zero, bud.")
        else:
            print("This DOES work")
            return answer
        finally:
            print("This should execute either way.")


print(simple_division())

a = input("number?")
