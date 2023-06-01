from collections import deque

kids = deque(input().split())
rotation_num = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-rotation_num)
    kid_that_lost = kids.popleft()
    print(f"Removed {kid_that_lost}")
print(f"Last is {kids.popleft()}")