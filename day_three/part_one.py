class Pointer:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def up(self, amount: int = 1):
        self.y -= amount

    def down(self, amount: int = 1):
        self.y += amount

    def right(self, amount: int = 1):
        self.x += amount

    def left(self, amount: int = 1):
        self.x -= amount

    def get(self, lines):
        if self.x >= len(lines[self.y]) - 1:
            self.x = self.x - (len(lines[self.y]) - 1)
        return lines[self.y][self.x]


class Frame:
    def __init__(self):
        self.lines = self.get_lines()

    def get_lines(self):
        file = open("./input")
        return file.readlines()

    def main(self):
        pointer = Pointer(0, 0)
        self.trees = 0
        for lines in self.lines:
            item = pointer.get(self.lines)
            if item == "#":
                self.trees += 1
            pointer.down()
            pointer.right(3)

if __name__ == "__main__":
    frame = Frame()
    frame.main()
    print(frame.trees)
