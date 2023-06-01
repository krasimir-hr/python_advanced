n = int(input())

matrix = [[int(x) for x in input().split(", ")] for y in range(n)]

primary_diagonal = []
secondary_diagonal = []
primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_num = matrix[i][i]
    primary_sum += primary_num
    primary_diagonal.append(primary_num)

    secondary_num = matrix[n-1-i][i]
    secondary_sum += secondary_num
    secondary_diagonal.append(secondary_num)

print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {primary_sum}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal[::-1]])}. Sum: {secondary_sum}')
