with open("../test_input") as file:
    lines = file.readlines()

number = 0
field = {"f": 1, "u": 1j, "d": -1j}


#   ^
#   |
# f |
#   +---->
#   u -- d

for line in lines:
    word, num = line.split(" ")
    num = int(num)

    print(num)

    if word[0] == "f":
        new = abs(number.imag * num) * 1j
        print(f"NEW: {new}")
        number += new

    print(number)
    number += field[word[0]] * num

number = int(abs(number.imag) * number.real)
print(number)
