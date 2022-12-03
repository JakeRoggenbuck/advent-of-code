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
ME_MAP = {"X": Turn.LOST, "Y": Turn.DRAW, "Z": Turn.WON}
MEO_MAP = {"X": Device.ROCK, "Y": Device.PAPER, "Z": Device.SCISSORS}


def two_wins(one: Device, two: Turn):
    if one == Device.ROCK:
        if two == Turn.DRAW:
            return Device.ROCK
        elif two == Turn.LOST:
            return Device.SCISSORS
        else:
            return Device.PAPER

    elif one == Device.PAPER:
        if two == Turn.DRAW:
            return Device.PAPER
        elif two == Turn.LOST:
            return Device.ROCK
        else:
            return Device.SCISSORS

    elif one == Device.SCISSORS:
        if two == Turn.DRAW:
            return Device.SCISSORS
        elif two == Turn.LOST:
            return Device.PAPER
        else:
            return Device.ROCK

score = 0

with open("input") as file:
    for line in file:
        a, b = line.split()

        e, m, = ELF_MAP[a], ME_MAP[b]
        win_state = two_wins(e, m)

        score += ME_MAP[b].value + win_state.value
        print(f"{MEO_MAP[b].value=}, {win_state.value=}, {ME_MAP[b]=}")

print(score)
