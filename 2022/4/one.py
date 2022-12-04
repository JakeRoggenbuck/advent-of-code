with open("input") as file:
    score = 0

    for line in file:
        first, second = line.split(",")

        f_start, f_finish = first.split("-")
        s_start, s_finish = second.split("-")

        f_start = int(f_start)
        f_finish = int(f_finish)
        s_start = int(s_start)
        s_finish = int(s_finish)

        if f_start <= s_start and f_finish >= s_finish:
            score += 1
        elif s_start <= f_start and s_finish >= f_finish:
            score += 1

    print(score)


