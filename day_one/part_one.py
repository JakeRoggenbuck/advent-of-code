from jakesutils.config import Config


day_one_input = Config("./input", "txt").config.split()
day_one_input = [int(num) for num in day_one_input]

for first_num in day_one_input:
    for second_num in day_one_input:
        if first_num + second_num == 2020:
            print(first_num * second_num)
            exit()
