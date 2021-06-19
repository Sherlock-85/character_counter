message = 'It was a bright warm day in June, and the clocks were striking noon.'
count = {}

for character in message.lower():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
