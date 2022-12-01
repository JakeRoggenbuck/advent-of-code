#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool check_and_modify(int *top, int total) {
    for (int i = 0; i < 3; i++) {
        if (total > top[i]) {
            int keep = top[1];
            switch (i) {
            case 0:
                top[1] = top[0];
            case 1:
                top[2] = keep;
            case 2:
                top[i] = total;
            }
            return true;
        }
    }
    return false;
}

int main() {
    FILE *fp;
    int bytes_read;
    size_t size = 10;
    char *line;
    int total = 0;
    int *top;

    top = calloc(3, sizeof(int));
    fp = fopen("input", "r");
    line = (char *)malloc(10 * sizeof(char));

    while ((bytes_read = getline(&line, &size, fp)) != -1) {
        if (bytes_read >= 5) {
            total += atoi(line);
        } else if (bytes_read == 1) {
            check_and_modify(top, total);
            total = 0;
        }
    }

	int sum = 0;
    for (int i = 0; i < 3; i++) {
        printf("%d\n", top[i]);
		sum += top[i];
    }
	printf("%d\n", sum);

    fclose(fp);
}
