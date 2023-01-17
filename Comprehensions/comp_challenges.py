# for x in range(1, 31):
#   fizzbuzz = "fizz buzz" if x % 5 == 0 and x % 3 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
#     print(fizzbuzz)

for x in range(1, 31):
    fizzbuzz_expression = ["fizz buzz" if x % 5 == 0 and x % 3 == 0
                           else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)]

fizz_range = range(1, 31)

fizzbuzz_list_comp = ['fizzbuzz' if x % 15 == 0
                      else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x)
                      for x in fizz_range]

print(fizzbuzz_list_comp)
