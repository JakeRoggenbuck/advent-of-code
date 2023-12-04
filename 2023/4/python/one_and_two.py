def one() -> int:
    isnum = lambda x: x.isnumeric()
    total = 0

    with open("../input") as file:
        for line in file:
            card, after = line.split(":")
            num = card[4:].strip()

            winning, actual = after.split("|")
            winning = winning.rstrip("\n")
            actual = actual.rstrip("\n")

            winning_list = set(filter(isnum, winning.split(" ")))
            actual_list = set(filter(isnum, actual.split(" ")))

            value = 0
            for w in winning_list:
                if w in actual_list:
                    if value == 0:
                        value = 1
                    else:
                        value *= 2

            total += value

    return total


def two() -> int:
    isnum = lambda x: x.isnumeric()

    with open("../input") as file:
        starting_cards = {}

        for line in file:
            card, after = line.split(":")
            num = card[4:].strip()

            winning, actual = after.split("|")
            winning = winning.rstrip("\n")
            actual = actual.rstrip("\n")

            winning_list = set(filter(isnum, winning.split(" ")))
            actual_list = set(filter(isnum, actual.split(" ")))

            starting_cards[int(num)] = (winning_list, actual_list)

        todo_list = list(range(1, len(starting_cards)+1))

        for todo in todo_list:
            winning, actual = starting_cards[todo]

            count = 0
            for w in winning:
                if w in actual:
                    count += 1

            to_add = list(range(todo+1, todo+count+1))
            todo_list.extend(to_add)

    return len(todo_list)


print(one())
print(two())
