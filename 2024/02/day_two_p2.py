INPUT = []

with open("./input") as file:
    for line in file:
        INPUT.append([int(a) for a in line.split()])


def check_invalid(line):
    i = 0
    is_inc = None

    invalid = 0
    invalid_indexes = []

    while i < len(line) - 1:
        if line[i] == line[i + 1]:
            invalid += 1
            invalid_indexes.append(i)
            i += 1
            continue

        if line[i] < line[i + 1]:
            if abs(line[i] - line[i + 1]) > 3:
                invalid += 1
                invalid_indexes.append(i)
                i += 1
                continue

            if is_inc is None:
                is_inc = True
            else:
                if not is_inc:
                    invalid += 1
                    invalid_indexes.append(i)
                    i += 1
                    continue

        if line[i] > line[i + 1]:
            if abs(line[i] - line[i + 1]) > 3:
                invalid += 1
                invalid_indexes.append(i)
                i += 1
                continue

            if is_inc is None:
                is_inc = False
            else:
                if is_inc:
                    invalid += 1
                    invalid_indexes.append(i)
                    i += 1
                    continue

        i += 1

    return invalid, invalid_indexes


safe_count = 0


for line in INPUT:
    invalid, invalid_indexes = check_invalid(line)
    if invalid == 0:
        safe_count += 1
        continue

    eventually = False
    for i in range(invalid_indexes[0]-1, invalid_indexes[0]+2):
        new_line = line[:i] + line[i+1:]
        a, b = check_invalid(new_line)
        if a == 0:
            eventually = True

    if eventually:
        safe_count += 1

print(safe_count)
