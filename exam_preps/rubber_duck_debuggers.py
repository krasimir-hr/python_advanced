from collections import deque

times = deque(int(x) for x in input().split())
tasks = [int(x) for x in input().split()]
duckies = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while times and tasks:
    time = times.popleft()
    task = tasks.pop()

    calculated_time = int(time * task)
    if 0 <= calculated_time <= 60:
        duckies["Darth Vader Ducky"] += 1
    elif 61 <= calculated_time <= 120:
        duckies["Thor Ducky"] += 1
    elif 121 <= calculated_time <= 180:
        duckies["Big Blue Rubber Ducky"] += 1
    elif 181 <= calculated_time <= 240:
        duckies["Small Yellow Rubber Ducky"] += 1
    else:
        times.append(time)
        tasks.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for ducky, count in duckies.items():
    print(f"{ducky}: {count}")
