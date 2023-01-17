menu = [
    ['egg', 'spam', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
    ['spam', 'egg', 'sausage', 'spam'],
    ['chicken', 'chips']
]

# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped")
# print(meals)
#
# meals_comprehension = [meal if 'spam' not in meal else "a meal was skipped" for meal in menu]
# print(meals_comprehension)
#
# x = 12
# expression = 'Twelve' if x == 12 else 'unknown'
# print(expression)

# for meal in menu:
#     print(f"{meal}:", 'contains sausage' if 'sausage' in meal else 'contains bacon' if 'bacon' in meal
#           else 'contains chicken' if 'chicken' in meal else 'contains egg' if 'egg' in meal
#           else "not really sure about this one ol' mate")

# print()
#
# items = set()
# for meal in menu:
#     for item in meal:
#         items.add(item)
# print(items)
# print()
#
# for meal in menu:
#     for item in items:
#         if item in meal:
#             print(f"{meal}:", f"contains {item}")
#             break


for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 5 == 0 and x % 3 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)
