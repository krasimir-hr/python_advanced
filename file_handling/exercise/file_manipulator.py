import os

while True:
    command_line = input().split("-")

    if command_line[0] == "End":
        break

    command, file_name, *info = command_line[0], command_line[1], *command_line

    if command == "Create":
        open(f"files/{file_name}", "w")

    elif command == "Add":
        content = command_line[2]
        with open(f"files/{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        try:
            with open(f"files/{file_name}", "r+") as file:
                text = file.read()
                text.replace(info[1], info[2])
                file.write(text)

        except FileNotFoundError:
            print(f"An error occurred")

    elif command == "Delete":
        if os.path.exists(f"files/{file_name}"):
            os.remove(f"files/{file_name}")
        else:
            print("An error occurred")
