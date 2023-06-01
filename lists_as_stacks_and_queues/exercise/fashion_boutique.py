box_of_clothes = [int(x) for x in input().split()]
capacity = int(input())
rack_counter = 0
current_rack = 0

while box_of_clothes:
    while len(box_of_clothes) > 0:
        if current_rack + box_of_clothes[-1] == capacity:
            rack_counter += 1
            current_rack = 0
            box_of_clothes.pop()
            break
        elif current_rack + box_of_clothes[-1] > capacity:
            rack_counter += 1
            current_rack = 0
            break
        else:
            current_rack += box_of_clothes.pop()

if current_rack != 0:
    print(rack_counter + 1)
else:
    print(rack_counter)