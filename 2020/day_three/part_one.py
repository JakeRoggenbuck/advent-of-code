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

    def get(self, line):
        if self.x >= len(line) - 1:
            self.x = self.x - (len(line) - 1)
        return line[self.x]


class Frame:
    def __init__(self):
        self.lines = self.get_lines()

    def get_lines(self):
        file = open("./input")
        return file.readlines()

    def main(self):
        pointer = Pointer(0, 0)
        self.trees = 0
        for line in self.lines:
            item = pointer.get(line)
            if item == "#":
                self.trees += 1
            pointer.down()
            pointer.right(3)

if __name__ == "__main__":
    frame = Frame()
    frame.main()
    print(frame.trees)
