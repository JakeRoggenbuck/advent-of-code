def list_comp():
    """This is a really funny list comp version"""
    with open("../input") as file:
        lines = file.readlines()

    n = [0]

    def field(x, b):
        n[0] += {"u": -1, "d": 1}[x[0]] * b

    number = sum(
        list(
            filter(
                lambda x: x is not None,
                [
                    b + (b * n[0]) * 1j if a[0] == "f" else field(a, b)
                    for (a, b) in [(c, int(d)) for (c, d) in [x.split() for x in lines]]
                ],
            )
        )
    )

    return int(number.imag * number.real)


def normal():
    with open("../input") as file:
        lines = file.readlines()

    aim, number = 0, 0
    field = lambda x: {"u": -1, "d": 1}[x[0]]

    for line in lines:
        word, num = line.split(" ")
        num = int(num)

        if word == "forward":
            number += num + (num * aim) * 1j
        else:
            aim += field(word) * num

    return int(number.imag * number.real)


if __name__ == "__main__":
    lc = list_comp()
    n = normal()

    print(lc, n)
