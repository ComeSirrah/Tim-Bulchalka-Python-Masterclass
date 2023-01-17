text = "What have the romans ever done for us?"

capitals = [char.upper() for char in text]

print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

lowercase_words = [word.lower() for word in text.split(' ')]
print(lowercase_words)