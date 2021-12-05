#include <fstream>
#include <iostream>
#include <string>
#define NUMSIZE 10

int main() {
    std::ifstream fp;
    fp.open("../input");

    std::string line;

    int last = 0;
    int num_increases = -1;
	int current;


    if (!fp.is_open()) {
		exit(1);
	}

	while (fp) {
		std::getline(fp, line);
		if (line != "") {
			current = stoi(line);
			if (current > last) {
				num_increases += 1;
			}
			last = current;
		}
	}

	std::cout << num_increases << std::endl;
    return 0;
}
