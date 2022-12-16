class Pointer:
    def __init__(self, cur: str):
        self.cur = cur
        self.paths: list[str] = [cur]

    def __add__(self, a: str):
        self.paths.append(a)
        self.cur = self.fullname()
        return self

    def back(self):
        self.paths.pop()

    def fullname(self):
        return '/'.join(self.paths)

    def make_iter(self):
        acc = []

        for c in self.paths:
            acc.append("/".join(acc) + c)

        return acc


VALS = {}
CUR = Pointer("/")

with open("input") as file:

    for line in file:
        cmd = line.split()

        # Any cd
        if cmd[0] == "$" and cmd[1] == "cd":
            # ..
            if cmd[2] == "..":
                CUR.back()
            # otherwise
            else:
                CUR += cmd[2]

        elif cmd[0].isdigit():
            size = int(cmd[0])

            for a in CUR.make_iter():
                if VALS.get(a):
                    VALS[a] += size
                else:
                    VALS[a] = size

    points = min(filter(lambda x: VALS["/"] - x <= 40000000, VALS.values()))
    print(points)
