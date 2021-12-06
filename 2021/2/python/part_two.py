def list_comp():
    """This is a really funny list comp version"""
    with open("../input") as file:
        lines = file.readlines()

    # Lists can be changed as side effects in function without that variable in
    # scope, so this works but n = 0 would not
    n = [0]

    def field(x, b):
        # Change the value of n based on if it should be negative or positive
        n[0] += {"u": -1, "d": 1}[x[0]] * b

    # Add up all of the complex numbers
    number = sum(
        list(
            # Remove all of the None
            filter(
                lambda x: x is not None,
                [
                    # The value is part real and part imaginary
                    # b is the real part, (b * n[0]) * 1j is imaginary because
                    # we we multiply by 1j

                    # field causes a side effect that changes the value of n
                    # because it should not be added up in the sum but we still
                    # need to keep track of it, so intentional side effects
                    b + (b * n[0]) * 1j if a[0] == "f" else field(a, b)
                    # For each line, split it, and make the second value an int
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
