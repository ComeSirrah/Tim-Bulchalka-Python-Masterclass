filename = 'Resources/Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "'wTasebv "
no_apostrophe = first.strip(chars)
print(no_apostrophe)

for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break
print('*'*80)
for character in first[::-1]: # process the string in reverse
    if character in chars:
        print(f'removing "{character} from the string.')
    else:
        break

print('*'*80)

twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = first.removesuffix('toves')
print(toves_removed)
