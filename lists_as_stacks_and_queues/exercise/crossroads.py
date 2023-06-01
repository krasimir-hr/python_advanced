from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
remaining_green = 0
remaining_free_window = 0
cars = deque()
crash = False
passed_cars = 0

while True:
    command = input()
    if command == "END":
        break

    elif command == "green":
        remaining_green = green_light_duration
        remaining_free_window = free_window_duration
        while cars:
            if crash:
                break
            if remaining_green == 0:
                break
            else:
                current_car = cars.popleft()
                passed_cars += 1
                for ch in current_car:
                    if remaining_green > 0:
                        remaining_green -= 1
                    else:
                        if remaining_free_window > 0:
                            remaining_free_window -= 1
                        else:
                            print("A crash happened!")
                            print(f"{current_car} was hit at {ch}.")
                            crash = True
                            break


    else:
        cars.append(command)

if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")