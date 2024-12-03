import re

data = ""
with open('day3.input.txt', 'r') as f:
    for line in f:
        data += line.strip()

# Part 1
total1 = 0

for i, j in re.findall(r'mul\((\d+),(\d+)\)', data):
    total1 += int(i) * int(j)

print("Total 1: " + str(total1))

# Part 2
total2 = 0

do_mul = True
for i, j, do, dont in re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', data):
    if do:
        do_mul = True
    elif dont:
        do_mul = False
    else:
        if do_mul:
            total2 += int(i) * int(j)

print("Total 2: " + str(total2))