def word_encode(line: str) -> str:
    build = ""

    for x in line:
        build += x

        build = build.replace("one", "1")
        build = build.replace("two", "2")
        build = build.replace("three", "3")
        build = build.replace("four", "4")
        build = build.replace("five", "5")
        build = build.replace("six", "6")
        build = build.replace("seven", "7")
        build = build.replace("eight", "8")
        build = build.replace("nine", "9")

    return build

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
        line = word_encode(line)

        val = find_nums(line)
        total += int(val)

print(total)
