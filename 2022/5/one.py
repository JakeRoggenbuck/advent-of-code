from pprint import pprint

STACKS = [
    "WBGZRDCV",
    "VTSBCFWG",
    "WNSBC",
    "PCVJNMGQ",
    "BHDFLST",
    "NMWTVJ",
    "GTSCLFP",
    "ZDB",
    "WZNM",
]

NEW = [[y for y in reversed(x)] for x in STACKS]

print(NEW)

with open("input") as file:
    for line in file:
        if "move" in line:
            _, a, _, b, _, c = line.split()

            for x in range(int(a)):
                NEW[int(c) - 1].append(NEW[int(b) - 1].pop())

for d in NEW:
    print(d[-1], end="")

print()
