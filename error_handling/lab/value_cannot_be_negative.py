class ValueCannotBeNegative(Exception):
    """Value cannot be negative"""
    pass


for i in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
