def factorial(n):
    assert 1 <= n < 901
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print(factorial(901))
except RecursionError:
    print("This program cannot calculate factorials that large")
except ZeroDivisionError:
    print("You need to fix this program, bud.")
except AssertionError:
    print("number must no less than 1 and no greater than 900")
print("Program terminating")