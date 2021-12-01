with open("./input") as file:
    lines = [int(x.strip()) for x in file.readlines()]

last = lines[0]
num_increases = 0
print(f"{last} (N/A - no previous measurement)")

for x in lines[1:]:
    if x > last:
        num_increases += 1
        print(f"{x} (increased)")
    else:
        print(f"{x} (decreased)")
    last = x

print(num_increases)
