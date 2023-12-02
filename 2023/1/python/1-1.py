def find_nums(line: str) -> str:
    a = ""
    b = ""

    for x in line:
        if x.isnumeric():
            a = x
            break

    for y in reversed(line):
        if y.isnumeric():
            b = y
            break

    return a + b


total = 0

with open("../input") as file:
    for line in file:

        val = find_nums(line)
        total += int(val)

print(total)
