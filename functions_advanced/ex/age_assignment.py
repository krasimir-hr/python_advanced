def age_assignment(*args, **kwargs):
    name_age = []
    result = ""
    for first_letter, age in kwargs.items():
        for name in args:
            if first_letter == name[0]:
                current_person = [name, age]
                name_age.append(current_person)
    sorted_persons = sorted(name_age, key=lambda x: x[0])
    for person in sorted_persons:
        result += f"{person[0]} is {person[1]} years old.\n"

    return result

print(age_assignment("Amy", "Bill", "Willy", W=36,
A=22, B=61))