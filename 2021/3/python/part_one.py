memory = [0] * 1
gamma = memory.copy()
epsilon = memory.copy()

with open("../input") as file:
    lines = file.readlines()

length = len(lines)
for line in lines:
    for x in range(0, 12):
        memory[x] += int(line[x])

for x, m in enumerate(memory):
    # Add the value to memory if m is greater than half of the length
    memory[x] = 1 if m > length / 2 else 0

gamma = [str(x) for x in memory]
# (not x) is a Boolean, so use int() to get it back to a number
epsilon = [str(int(not x)) for x in memory]

# Convert binary to int
gamma_value = int("".join(gamma), 2)
epsilon_value = int("".join(epsilon), 2)

print(f"{gamma_value=}, {epsilon_value=}")

print(gamma_value * epsilon_value)
