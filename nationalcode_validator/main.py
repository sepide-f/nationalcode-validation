import json

with open('data.json') as user_file:
    file_contents = user_file.read()
    region = json.loads(file_contents)


def national_code_validator(code: str) -> any:
    if not code.isdigit():
        return "please enter a digit"

    if len(code) != 10:
        return "please enter 10 digits"

    summ = 0
    for i in range(10, 1, -1):
        summ += i * int(code[10 - i])

    remainder = summ % 11

    if (remainder < 2 and remainder == int(code[-1])) or (remainder >= 2 and int(code[-1]) == 11 - remainder):
        y = code[:3]
        return True, region.get(y, "Unknown region")
    else:
        return False


