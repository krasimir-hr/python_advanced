email = "krasio@abv.bg"

parts = email.split("@")

domain = parts[1].split("."[-1])[1]

print(domain)