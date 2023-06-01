chemicals = set()

for _ in range(int(input())):
    elements = input().split()
    for element in elements:
        chemicals.add(element)

print(*chemicals, sep="\n")
