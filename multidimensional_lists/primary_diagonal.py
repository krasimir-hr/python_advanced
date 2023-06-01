n = int(input())

matrix = [[int(x) for x in input().split()] for row in range(n)]
diagonal_sum = 0

for i in range(n):
        diagonal_sum += matrix[i][i]

print(diagonal_sum)