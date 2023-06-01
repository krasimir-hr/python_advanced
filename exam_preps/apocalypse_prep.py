from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

inventory = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}
leftover = 0

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    current_sum = current_textile + current_medicament

    if current_sum == 30:
        inventory["Patch"] += 1

    elif current_sum == 40:
        inventory["Bandage"] += 1

    elif current_sum == 100:
        inventory["MedKit"] += 1

    elif current_sum > 100:
        inventory["MedKit"] += 1
        current_sum -= 100
        medicaments[-1] += current_sum

    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textiles and medicaments:
    print("Textiles are empty.")

elif textiles and not medicaments:
    print("Medicaments are empty.")

sorted_inventory = sorted(inventory.items(), key=lambda x: (-x[1], x[0]))

for item, quantity in sorted_inventory:
    if quantity == 0:
        continue
    print(f"{item} - {quantity}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments])}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")