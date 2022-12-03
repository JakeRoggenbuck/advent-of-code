def check_dup(first, second):
    for c in first:
        if c in second:
            return c


def check_dups(first, second):
    dups = []
    for c in first:
        if c in second:
            dups.append(c)
    return dups


def check_dups_new(first, second, third):
    for c in first:
        if c in second and c in third:
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
    index = 0
    last_three = []

    for x in file:
        length = len(x)
        half = length // 2
        # first, second = x[:half], x[half:]

        # dups = check_dups(first, second)

        last_three.append(x)

        if index < 2:
            index += 1
        else:

            #     for b in last_three[0]:
            #         print("0th", last_three[0])
            #         if b in last_three[1] and b in last_three[2]:
            #             print(last_three)
            #             print(b)

            dups = check_dups_new(*last_three)
            score += rank(dups)
            last_three = []
            index = 0

        # score += rank(dup)

print(score)
