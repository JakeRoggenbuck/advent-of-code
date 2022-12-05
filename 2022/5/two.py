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

            stage = []
            for x in range(int(a)):
                stage.append(NEW[int(b) - 1].pop())

            for s in reversed(stage):
                NEW[int(c) - 1].append(s)

for d in NEW:
    print(d[-1], end="")

print()
