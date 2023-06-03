class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class MoreThanOneDotError(Exception):
    pass


VALID_DOMAINS = ['com', 'bg', 'org', 'net']

while True:
    emails_line = input()
    if emails_line == 'End':
        break

    list_of_email = emails_line.split('@')

    email_name = list_of_email[0]
    if len(email_name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if '@' not in emails_line:
        raise MustContainAtSymbolError("Email must contain @")

    domain_name = emails_line.split('.')
    if domain_name[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if emails_line.count('@') > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol")

    if emails_line.count('.') > 1:
        raise MoreThanOneDotError("Email should contain only one '.' symbol")

    print('Email is valid')