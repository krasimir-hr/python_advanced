file = open("numbers.txt", "r")
total_sum = 0

for line in file:
    total_sum += int(line)

print(total_sum)
