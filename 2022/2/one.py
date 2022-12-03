from enum import Enum


class Device(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Turn(Enum):
    WON = 6
    DRAW = 3
    LOST = 0


ELF_MAP = {"A": Device.ROCK, "B": Device.PAPER, "C": Device.SCISSORS}
ME_MAP = {"X": Device.ROCK, "Y": Device.PAPER, "Z": Device.SCISSORS}


def two_wins(one: Device, two: Device):
    if one == Device.ROCK:
        if two == Device.ROCK:
            return Turn.DRAW
        elif two == Device.PAPER:
            return Turn.WON
        elif two == Device.SCISSORS:
            return Turn.LOST

    elif one == Device.PAPER:
        if two == Device.ROCK:
            return Turn.LOST
        elif two == Device.PAPER:
            return Turn.DRAW
        elif two == Device.SCISSORS:
            return Turn.WON

    elif one == Device.SCISSORS:
        if two == Device.ROCK:
            return Turn.WON
        elif two == Device.PAPER:
            return Turn.LOST
        elif two == Device.SCISSORS:
            return Turn.DRAW

score = 0

with open("input") as file:
    for line in file:
        a, b = line.split()

        e, m, = ELF_MAP[a], ME_MAP[b]
        win_state = two_wins(e, m)

        score += m.value + win_state.value

print(score)
