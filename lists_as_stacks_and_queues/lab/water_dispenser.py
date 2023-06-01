from collections import deque

water_quantity = int(input())
line_of_people = deque()

while True:
    name = input()
    if name == "Start":
        break
    else:
        line_of_people.append(name)

while True:
    command = input()
    if command == "End":
        break
    data = command.split()
    if data[0] == "refill":
        liters_added = int(data[1])
        water_quantity += liters_added
    else:
        liters_needed = int(data[0])
        if water_quantity >= liters_needed:
            water_quantity -= liters_needed
            print(f"{line_of_people.popleft()} got water")
        else:
            print(f"{line_of_people.popleft()} must wait")

print(f"{water_quantity} liters left")