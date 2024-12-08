text = ""

with open("./input") as file:
    for line in file:
        text += line

# Add padding
text += " " * 20

count = 0

i = 0
while i < len(text):
    c = text[i]

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
                count += int(a) * int(b)

    i += 1

print(count)
