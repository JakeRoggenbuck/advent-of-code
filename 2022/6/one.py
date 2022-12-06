with open("input") as file:
    count = 4

    index = 0
    cont = file.read()
    box = [x for x in cont[:4]]

    for char in cont[5:]:
        count += 1

        ori = box.copy()
        box = box[1:]
        box.append(char)

        index += 1

        if len(set(ori)) == 4:
            print(index + 3)
            break

    print(count)
