import shlex


class Line:
    def __init__(self, raw_line: str):
        self.raw_line = raw_line
        self.shlex_parts()

    def shlex_parts(self):
        num_range, letter, self.password = shlex.split(self.raw_line)
        self.first_num, self.second_num = [int(num) for num in num_range.split("-")]
        self.letter = letter[0]
        print(raw_line, [self.first_num, self.second_num, self.letter, self.password])

    def check(self) -> bool:
        first = self.password[self.first_num-1] == self.letter
        second = self.password[self.second_num-1] == self.letter
        if first != second:
            return True


valid = 0
for raw_line in open("./input").readlines():
    line = Line(raw_line)
    if line.check():
        valid += 1

print(valid)
