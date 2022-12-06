with open("input") as file:
    count = 14

    index = 0
    cont = file.read()
    box = [x for x in cont[:14]]

    for char in cont[15:]:
        count += 1

        ori = box.copy()
        box = box[1:]
        box.append(char)

        index += 1

        if len(set(ori)) == 14:
            print(index + 3)
            break

    print(count)


