import enum


class ItemType(enum.Enum):
    CHAR = 1
    NUM = 2


class Item:
    def __init__(self, item_type: ItemType, value, start: int, end: int):
        self.start = start
        self.end = end
        self.item_type: ItemType = item_type
        self.value = value
        self.is_part = False

    def __str__(self):
        if self.is_part:
            return f" ({self.value}) "
        else:
            return f" {self.value} "

    def __repr__(self):
        return self.__str__()

    def adjacent_to(self, item) -> bool:
        if item.item_type == ItemType.NUM:
            return False

        if item.start >= self.start - 2 and item.start <= self.end:
            return True

        return False

    def is_part_check(self, lines) -> bool:
        for line in lines:
            for item in line:
                if self.adjacent_to(item):
                    return True

        return False

    def set_is_part(self, lines):
        if self.item_type == ItemType.CHAR:
            return

        self.is_part = self.is_part_check(lines)

    def adjacent_nums(self, item):
        if item.item_type == ItemType.CHAR:
            return

        if self.start >= item.start - 2 and self.start <= item.end:
            return item

    def get_adjacent_nums(self, lines):
        nums = []
        for line in lines:
            for item in line:
                a = self.adjacent_nums(item)
                if a is not None:
                    nums.append(a)
        return nums

lines = []

with open("../input") as file:
    line_num = 0
    for line in file:
        in_num = False
        current_num = ""

        lines.append([])

        for n, c in enumerate(line):
            if not c.isnumeric() and c != "." and c != "\n":

                if current_num != "":
                    lines[line_num].append(
                        Item(
                            ItemType.NUM,
                            current_num,
                            n - len(current_num) + 1,
                            n
                        )
                    )

                    current_num = ""
                in_num = False
                lines[line_num].append(Item(ItemType.CHAR, c, n, n))
                continue

            if not in_num and c.isnumeric():
                in_num = True

            if in_num and not c.isnumeric():
                in_num = False
                lines[line_num].append(
                    Item(
                        ItemType.NUM,
                        current_num,
                        n - len(current_num) + 1,
                        n
                    )
                )

                current_num = ""

            if in_num:
                current_num += c

        line_num += 1


total = 0
line_count = 0
for value in lines:

    before = line_count - 1
    if before < 1:
        before = 0

    after = line_count + 1
    if after > len(lines) - 1:
        after = len(lines) - 1

    for item in value:
        if item.value == "*":
            nums = item.get_adjacent_nums(lines[before:after + 1])
            if len(nums) == 2:
                total += (int(nums[0].value) * int(nums[1].value))

    line_count += 1

print(total)
