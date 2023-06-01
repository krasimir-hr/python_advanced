from collections import deque

rows, cols = [int(x) for x in input().split()]
string = list(input())
string_copy = deque(string.copy())


for i in range(rows):
    while len(string_copy) < cols:
        string_copy.extend(string)
    if i % 2 == 0:
        print(*[string_copy.popleft() for j in range(cols)], sep="")

    else:
        print(*[string_copy.popleft() for j in range(cols)][::-1], sep="")