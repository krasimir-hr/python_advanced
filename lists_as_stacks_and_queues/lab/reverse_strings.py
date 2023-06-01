string = input()

stack_text = list(string)

while stack_text:
    removed_element = stack_text.pop()
    print(removed_element, end='')
