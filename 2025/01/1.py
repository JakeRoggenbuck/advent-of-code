with open("./input") as file:
    lines = [a.rstrip() for a in file.readlines()]

rotation = 50
zero_count = 0

for line in lines:
    direction, amount = line[0], line[1:]
    amount = int(amount)

    if direction == "R":
        rotation += amount
    elif direction == "L":
        rotation -= amount

    # overflow / underflow
    rotation %= 100

    print(rotation)

    # zero check
    if rotation == 0:
        zero_count += 1

print(f"{zero_count=}")
