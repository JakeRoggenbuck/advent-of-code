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

        fi = list(range(f_start, f_finish+1))
        si = list(range(s_start, s_finish+1))

        if f_finish in si or f_start in si:
            score += 1
        elif s_finish in fi or s_start in fi:
            score += 1


    print(score)


