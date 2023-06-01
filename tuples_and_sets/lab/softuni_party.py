guest_list_vip = set()
guest_list_regular = set()

for _ in range(int(input())):
    res_num = input()
    if res_num[0].isdigit():
        guest_list_vip.add(res_num)
    else:
        guest_list_regular.add(res_num)

while True:
    current_guest = input()
    if current_guest == "END":
        break
    elif current_guest in guest_list_vip:
        guest_list_vip.remove(current_guest)
    elif current_guest in guest_list_regular:
        guest_list_regular.remove(current_guest)


print(len(guest_list_regular) + len(guest_list_vip))
for guest in sorted(guest_list_vip):
    print(guest)

for guest in sorted(guest_list_regular):
    print(guest)
    