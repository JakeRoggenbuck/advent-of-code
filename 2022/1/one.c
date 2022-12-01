#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    int bytes_read;
    size_t size = 10;
    char *line;

    int largest = 0;
    int total = 0;

    fp = fopen("input", "r");
    while ((bytes_read = getline(&line, &size, fp)) != -1) {
        if (bytes_read >= 5) {
            total += atoi(line);
        } else if (bytes_read == 1) {
            if (total > largest) {
                largest = total;
            }
            total = 0;
        }
    }

    printf("%d\n", largest);

    fclose(fp);
}
