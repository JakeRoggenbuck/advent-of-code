class Sheet:
    def __init__(self):
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)


with open("../input") as file:
    lines = file.readlines()
    first_list = list(map(int, lines[0].split(",")))

in_sheet = False
current = None

for line in lines:
    new_line = list(map(int, line.split(",")))
    if not in_sheet:
        current = Sheet()
    current.add_line(new_line)


print(first_list)
