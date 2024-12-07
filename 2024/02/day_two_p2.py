INPUT = []

with open("./input") as file:
    for line in file:
        INPUT.append([int(a) for a in line.split()])

safe_count = 0

def check_safe(line, removed_error, before):
    if removed_error:
        print(before, line)
    else:
        print(line)

    i = 0
    is_inc = None

    invalid = False

    while i < len(line) - 1:
        if line[i] == line[i + 1]:
            if removed_error:
                invalid = True
                break
            else:
                return check_safe(line[:i] + line[i+1:], True, line) and check_safe(line[:i+1] + line[i+2:], True, line)

        if line[i] < line[i + 1]:
            if abs(line[i] - line[i + 1]) > 3:
                if removed_error:
                    invalid = True
                    break
                else:
                    return check_safe(line[:i] + line[i+1:], True, line) and check_safe(line[:i+1] + line[i+2:], True, line)

            if is_inc is None:
                is_inc = True
            else:
                if not is_inc:
                    if removed_error:
                        invalid = True
                        break
                    else:
                        return check_safe(line[:i] + line[i+1:], True, line) and check_safe(line[:i+1] + line[i+2:], True, line)

        if line[i] > line[i + 1]:
            if abs(line[i] - line[i + 1]) > 3:
                    if removed_error:
                        invalid = True
                        break
                    else:
                        return check_safe(line[:i] + line[i+1:], True, line) and check_safe(line[:i+1] + line[i+2:], True, line)

            if is_inc is None:
                is_inc = False
            else:
                if is_inc:
                    if removed_error:
                        invalid = True
                        break
                    else:
                        return check_safe(line[:i] + line[i+1:], True, line) and check_safe(line[:i+1] + line[i+2:], True, line)

        i += 1

    return invalid

for line in INPUT:
    invalid = check_safe(line, False, None)

    if not invalid:
        safe_count += 1


print(safe_count)
