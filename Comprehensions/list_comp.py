print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Choose a number. I'll give you its square."))

squares = [number ** 2 for number in numbers]

index_pos = numbers.index(number)
print(squares[index_pos])
