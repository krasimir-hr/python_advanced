def fill_the_box(height, length, width, *cubes):
    volume = height * length * width
    total_cubes = 0
    for cube in cubes:
        if cube == "Finish":
            break
        total_cubes += cube
    if volume > total_cubes:
        return f"There is free space in the box. You could put {volume - total_cubes} more cubes."
    else:
        return f"No more free space! You have {total_cubes - volume} more cubes."

print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))