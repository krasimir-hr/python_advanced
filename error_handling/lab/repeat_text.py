try:
    word = input()
    times = int(input())
    print(word * times)

except ValueError:
    print("Variable times must be an integer")
