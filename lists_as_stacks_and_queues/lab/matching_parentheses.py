text = input()
stack_parent = []

for idx in range(len(text)):
    if text[idx] == "(":
        stack_parent.append(idx)
    elif text[idx] == ")":
        start_pos = stack_parent.pop()
        end_pos = idx + 1
        print(text[start_pos:end_pos])
