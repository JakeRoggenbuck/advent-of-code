def check_dup(first, second):
    for c in first:
        if c in second:
            return c


def isupper(c):
    if c >= 'A' and c <= 'Z':
        return True
    else:
        return False


def rank(val):
    a = ord(val)
    if isupper(val):
        return a - 38
    else:
        return a - 96

score = 0

with open("input") as file:
    for x in file:
        length = len(x)
        half = length // 2
        first, second = x[:half], x[half:]

        dup = check_dup(first, second)
        score += rank(dup)

print(score)
