l_one = []
l_two = []

with open("./input") as file:
    for line in file:
        a, b = line.split()
        l_one.append(int(a))
        l_two.append(int(b))

l_one.sort()
l_two.sort()

part_one_out = sum([abs(y - x) for x, y in zip(l_one, l_two)])

part_two_out = sum([x * l_two.count(x) for x in l_one])

print(part_one_out, part_two_out)
