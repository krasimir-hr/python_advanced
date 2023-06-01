from re import findall


class NameTooShortError(Exception):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""


accepted_domains = (".com", ".bg", ".org", ".net")
pattern_domain = r'\.[a-z]+'

while True:
    current_email = input()
    if current_email == "End":
        break

    if "@" not in current_email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(current_email.split("@")[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    if findall(pattern_domain, current_email)[-1] not in accepted_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
