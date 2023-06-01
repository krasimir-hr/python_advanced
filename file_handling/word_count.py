with open("words.txt", "w") as words_file:
    words_file.write("quick is fault")

word_count = {}

for word in words_file:
    word_count[word] = 0

with open("input.txt", "w") as input_file:
    input_file.write("-I was quick to judge him, but it wasn't his fault.")
    input_file.write("-Is this some kind of joke?! Is it?")
    input_file.write("-Quick, hide here...It is safer.")


print(word_count)