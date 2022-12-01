#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    size_t len = 6;
    char *line;
    size_t size;

    int largest = 0;
    int total = 0;

    fp = fopen("input", "r");
    while ((size = getline(&line, &len, fp)) != -1) {
        if (size >= 5) {
            total += atoi(line);
        } else if (size == 1) {
            if (total > largest) {
                largest = total;
            }
            total = 0;
        }
    }

    printf("%d\n", largest);

    fclose(fp);
}
