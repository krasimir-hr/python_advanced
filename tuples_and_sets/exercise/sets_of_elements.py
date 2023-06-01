nums = [int(x) for x in input().split()]

first_list = set()
second_list = set()

for _ in range(nums[0]):
    num = input()
    first_list.add(num)

for _ in range(nums[1]):
    num = input()
    second_list.add(num)

print(*first_list.intersection(second_list), sep="\n")
