from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_nectar = 0

functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}

while bees and nectars:
    current_bee = bees.popleft()
    current_nectar = nectars.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
    elif current_nectar > current_bee:
        total_nectar += abs(functions[symbols.popleft()](current_bee, current_nectar))

print(f"Total honey made: {total_nectar}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")