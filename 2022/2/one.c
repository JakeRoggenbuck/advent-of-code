#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum Dev { ROCK = 1, PAPER = 2, SCISSORS = 3 };
enum Turn { WON = 6, DRAW = 3, LOST = 0 };

const enum Dev DEVS[3] = {ROCK, PAPER, SCISSORS};

enum Dev from_elf(char *c) { return DEVS[(int)c - 65]; }
enum Dev from_me(char *c) { return DEVS[(int)c - 88]; }

enum Turn two_wins(enum Dev one, enum Dev two) {
    if (one == ROCK) {
        if (two == ROCK) {
            return DRAW;
        } else if (two == PAPER) {
            return WON;
        } else if (two == SCISSORS) {
            return LOST;
        }
    } else if (one == PAPER) {
        if (two == ROCK) {
            return LOST;
        } else if (two == PAPER) {
            return DRAW;
        } else if (two == SCISSORS) {
            return WON;
        }
    } else if (one == SCISSORS) {
        if (two == ROCK) {
            return WON;
        } else if (two == PAPER) {
            return LOST;
        } else if (two == SCISSORS) {
            return DRAW;
        }
    }
}

int main() {
    FILE *fp;

    int bytes_read = 0;
    size_t size = 10;
    char *line;
    char first;
    char second;

    enum Dev elf;
    enum Dev me;
    enum Turn outcome;
    int score = 0;

    line = malloc(10 * sizeof(char));
    fp = fopen("input", "r");
    while ((bytes_read = getline(&line, &size, fp)) != -1) {
        first = line[0];
        second = line[2];

        elf = from_elf(first);
        me = from_me(second);

        outcome = two_wins(elf, me);
        score += outcome + me;
    }

    printf("score: %d\n", score);

    fclose(fp);
}
