text = input()
set_of_letters = {}

for letter in text:
    if letter not in set_of_letters:
        set_of_letters[letter] = 0
    set_of_letters[letter] += 1


set_of_letters = dict(sorted(set_of_letters.items()))

for letter, occurrance in set_of_letters.items():
    print(f'{letter}: {occurrance} time/s')