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

number = int(number.imag * number.real)
print(number)
