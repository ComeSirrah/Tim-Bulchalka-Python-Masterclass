# numbers = set()

# print(type(numbers))

# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)
# print()

data = ['blue', 'red', 'blue', 'green', 'red', 'blue', 'white']

# unique_data = list(dict.fromkeys(data, 0))
# print(unique_data)
# print()
# print(dict.fromkeys(data, 0))

color_count = dict.fromkeys(data, 0)
for color in data:
    color_count[color] += 1

print(color_count)
