def cookie(presents_left, nice_kids):
    for coordinates in directions.values():  # обхождаме всяка посока от посоките
        r = santa_pos[0] + coordinates[0]  # намираме реда като съберем реда на Дядо Коледа и реда от посоката
        c = santa_pos[1] + coordinates[1]  # намираме колоната като съберем колоната на Дядо Коледа и тази от посоката

        if neighbourhood[r][c].isalpha():  # проверяваме дали сме стъпили на буква
            if neighbourhood[r][c] == 'V':  # проверяваме дали сме в къщата на добро дете
                nice_kids += 1  # увеличаваме броя на посетените добри деца за скоупа на функцията

            neighbourhood[r][c] = '-'  # заменяме позицията, на която сме с тире
            presents_left -= 1  # намаляме наличните подаръци с 1, в скоупа на функцията

        if not presents_left:  # проверяваме дали са ни свършили подаръците
            break  # прекратяваме цикъла

    return presents_left, nice_kids  # връщаме наличните подаръци и броя на посетените добри деца


presents = int(input())
SIZE = int(input())

neighbourhood = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

total_nice_kids = 0
nice_kids_visited = 0
santa_pos = []

for row in range(SIZE):
    neighbourhood.append(input().split())
    if "S" in neighbourhood[row]:
        santa_pos = [row, neighbourhood[row].index("S")]
        neighbourhood[row][santa_pos[1]] = "-"
    total_nice_kids += neighbourhood[row].count("V")


while True:
    direction = input()

    if direction == "Christmas morning":
        break

    santa_pos = [
        santa_pos[0] + directions[direction][0],
        santa_pos[1] + directions[direction][1],
    ]
    house = neighbourhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        presents -= 1
        nice_kids_visited += 1

    elif house == "C":
        presents, nice_kids_visited = cookie(presents, nice_kids_visited)

    neighbourhood[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kids_visited == total_nice_kids:
        break

neighbourhood[santa_pos[0]][santa_pos[1]] = "S"

if not presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

print(*[' '.join(row) for row in neighbourhood], sep='\n')
if total_nice_kids == nice_kids_visited:
    print(f"Good job, Santa! {nice_kids_visited} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")
