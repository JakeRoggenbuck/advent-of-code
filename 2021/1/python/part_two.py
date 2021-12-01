with open("../input") as file:
    lines = [int(x.strip()) for x in file.readlines()]

A = lines[0]
B = lines[1]
C = lines[2]

z = A + B + C

last = z

num_increases = 0
print(f"{z} (N/A - no previous measurement)")

i = 1
while i < len(lines) - 2:
    α, β, γ = lines[i:i+3]
    Σ = α + β + γ
    if Σ > last:
        print(f"{Σ} (increased)")
        num_increases += 1
    else:
        print(f"{Σ} (decreased)")
    last = Σ

    i += 1

print(num_increases)
