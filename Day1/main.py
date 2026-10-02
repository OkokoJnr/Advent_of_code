sequence = open("input.txt").readlines()
total = 50
count = 0
for rotate in sequence:
    sign = rotate[0]
    turns = int(rotate[1:])
    if sign == "L":
        total -= turns
        if total < 0:
            total = total % 100
    elif sign == "R":
        total += turns
        if total >=100:
            total = total%100
    if total == 0:
        count += 1

print(count)
    