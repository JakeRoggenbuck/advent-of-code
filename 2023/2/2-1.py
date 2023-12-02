with open("input") as file:
    total = 0

    real_maxes = {"green": 13, "blue": 14, "red": 12}

    for line in file:
        line = line.rstrip("\n")

        game, values = line.split(":")

        _, id = game.split(" ")

        sets = values.split(";")

        maxes = {"green": 0, "blue": 0, "red": 0}

        for x in sets:
            z = x.split(",")

            for a in z:
                a = a.lstrip(" ")
                num, word = a.split(" ")
                if int(maxes[word]) < int(num):
                    maxes[word] = int(num)

        valid = True
        for ((bk, bv), (ck, cv)) in zip(real_maxes.items(), maxes.items()):
            print(cv, bv)
            if cv > bv:
                valid = False

        if valid:
            total += int(id)

print(total)
