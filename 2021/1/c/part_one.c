#include <stdio.h>
#include <stdlib.h>
#define NUMSIZE 10

int main() {
    char c;
    char filename[] = "../input";
    char current_char[NUMSIZE] = "";
    char current_index = 0;

    int last = 0;
    int num_increases = -1;
    int current_number = 0;

    FILE *fp;

    fp = fopen(filename, "r");

    if (fp == NULL) {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }

    while ((c = fgetc(fp)) != EOF) {
        if (c == '\n') {
            current_number = atoi(current_char);
            current_index = 0;
            if (current_number > last) {
                num_increases += 1;
            }
        }
        current_char[current_index] = c;
		current_index += 1;
		last = current_number;
    }

    printf("%d\n", num_increases);

    fclose(fp);

    return 0;
}
