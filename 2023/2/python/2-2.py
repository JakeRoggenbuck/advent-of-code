with open("../input") as file:
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

        total += maxes["green"] * maxes["blue"] * maxes["red"]


print(total)
