from sys import maxsize
ranges = []
longest_intersection_size = -maxsize

for _ in range(int(input())):
    data = input().split("-")
    first_nums = data[0]
    seconds_nums = data[1]
    ranges += [first_nums, seconds_nums]

for idx in range(0, len(ranges), 2):
    first_range = ranges[idx]
    second_range = ranges[idx+1]

    data_first = first_range.split(",")
    first_start = int(data_first[0])
    first_end = int(data_first[1])
    first_set = set()
    current_num = int(first_start)
    while current_num <= first_end:
        first_set.add(current_num)
        current_num += 1

    data_second = second_range.split(",")
    second_start = int(data_second[0])
    second_end = int(data_second[1])
    second_set = set()
    current_num = int(second_start)
    while current_num <= second_end:
        second_set.add(current_num)
        current_num += 1

    intersec = first_set.intersection(second_set)
    if len(intersec) > longest_intersection_size:
        longest_intersection_size = len(intersec)
        longest_intersection = intersec

print(f"Longest intersection is {list(longest_intersection)} with length {longest_intersection_size}")
