INPUT = []

with open("./input") as file:
    for line in file:
        INPUT.append([int(a) for a in line.split()])

safe_count = 0

for line in INPUT:
    i = 0
    is_inc = None

    invalid = False

    while i < len(line) - 1:
        if line[i] == line[i + 1]:
            invalid = True
            break

        if line[i] < line[i + 1]:
            if abs(line[i] - line[i + 1]) > 3:
                invalid = True
                break

            if is_inc is None:
                is_inc = True
            else:
                if not is_inc:
                    invalid = True
                    break

        if line[i] > line[i + 1]:
            if abs(line[i] - line[i + 1]) > 3:
                invalid = True
                break

            if is_inc is None:
                is_inc = False
            else:
                if is_inc:
                    invalid = True
                    break

        i += 1

    if not invalid:
        safe_count += 1
        print(line)


print(safe_count)
