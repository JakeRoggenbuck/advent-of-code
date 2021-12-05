with open("../input") as file:
    lines = [int(x.strip()) for x in file.readlines()]

last = lines[0]
num_increases = 0

for x in lines[1:]:
    if x > last:
        num_increases += 1
    last = x

print(num_increases)
