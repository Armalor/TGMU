# Срезы:

string = 'А роза упала на лапу Азора'


def is_palindrome(string: str) -> bool:
    spaceless = [k.upper() for k in string if k != ' ']

    return spaceless == spaceless[::-1]


ret = is_palindrome(string)

print(ret)

