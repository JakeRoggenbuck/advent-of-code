text = ""

with open("./input") as file:
    for line in file:
        text += line

# Add padding
text += " " * 20

count = 0

i = 0
should_done = True
while i < len(text):
    c = text[i]

    if c == "d":
        if text[i+1:i+4] == "o()":
            should_done = True

        if text[i+1:i+7] == "on't()":
            should_done = False

    if c == "m":
        full = text[i+1:i+12]

        if full[:2] != "ul":
            i += 1
            continue

        if full[2] != "(":
            i += 1
            continue

        full = full.split(")")[0]
        full = full[3:]

        out = full.split(",")
        if len(out) == 2:
            a, b = out

            if a.isdigit() and b.isdigit():
                if should_done:
                    count += int(a) * int(b)

    i += 1

print(count)
