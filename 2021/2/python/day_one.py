def non_golf():
    with open("../input") as file:
        lines = file.readlines()

    number = 0

    field = {"forward": 1, "up": 1j, "down": -1j}

    for line in lines:
        word, num = line.split(" ")
        number += field[word] * int(num)

    number = int(abs(number.imag) * number.real)
    print(number)


def golf():
    """This is bad code, this is golfed sorta, never do this"""
    f=open("../input")
    l=f.readlines()
    n=0
    d={"f":1,"u":1j,"d":-1j}
    for a in l:
        w,m=a.split(" ")
        n+=d[w[0]]*int(m)
    n=int(abs(n.imag)*n.real)
    print(n)
    f.close()

if __name__ == "__main__":
    golf()
