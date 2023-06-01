from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted = []

toys = {150: "Doll",
        250: "Wooden train",
        300: "Teddy bear",
        400: "Bicycle",
}

while materials and magic_levels:
    curr_material = materials.pop() if magic_levels[0] or not materials[0] else 0
    curr_magic_level = magic_levels.popleft() if curr_material or not magic_levels[0] else 0

    if not curr_magic_level:
        continue

    product = curr_material * curr_magic_level

    if toys.get(product):
        crafted.append(toys[product])
    elif product < 0:
        materials.append(curr_material + curr_magic_level)
    elif product > 0:
        materials.append(curr_material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")


[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]