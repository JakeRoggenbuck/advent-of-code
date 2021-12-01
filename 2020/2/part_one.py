import shlex


class Line:
    def __init__(self, raw_line: str):
        self.raw_line = raw_line
        self.shlex_parts()

    def shlex_parts(self):
        split = shlex.split(self.raw_line)
        num_range, letter, self.password = split
        self.smol_num, self.large_num = [int(num) for num in num_range.split("-")]
        self.letter = letter[:-1]

    def display(self):
        print(f"There is between {self.smol_num} and {self.large_num} of {self.letter} in {self.password}")

    def check(self) -> bool:
        amount = self.password.count(self.letter)
        if self.smol_num <= amount and self.large_num >= amount:
            return True


valid = 0
verbose = False
for raw_line in open("./input").readlines():
    line = Line(raw_line)
    if line.check():
        if verbose: line.display()
        valid += 1

print(valid)
