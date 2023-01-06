# def print_backwards(*args, end=' ', **kwargs):
#     for word in args[::-1]:
#         print(word[::-1], end=end, **kwargs)


def print_backwards(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


# with open('backwards.txt', "w", encoding="UTF-8") as backwards:
print_backwards("hello", "planet", "earth", "take", "me", "to", "your",
                "leader")

# anime_list = ['One Piece', 'Cyberpunk Edgerunners', 'Rouroni Kenshin',
#               'Cowboy Bebop', 'Gargantia and the Verdurous Planet']
# anime_dict = {'One Piece': 'A true epic',
#               'Cyberpunk Edgerunners': 'Gritty and depressing',
#               'Rouroni Kenshin': 'A timeless tale',
#               'Cowboy Bebop': 'I dig noir',
#               'Gargantia and the Verdurous Planet': 'Short and sweet'}
#
# print(anime_list)
# print('*' * 80)
# print(*anime_list)
# print('*' * 80)
# print('*' * 80)
# print()
# print(anime_dict)
# print('*' * 80)
# print(*anime_dict, sep=", ")
# print('*' * 80)
# print('*' * 80)
# *numbers, = range(5)
# print(numbers)
