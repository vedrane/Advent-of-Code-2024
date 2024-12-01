# Part 1

left = []
right = []

with open('day1.input.txt', 'r') as f:
    for line in f:
        left.append(int(line.split('   ')[0]))
        right.append(int(line.split('   ')[1]))

left.sort()
right.sort()

total1 = 0
for i in range(len(left)):
    total1 += (abs(left[i] - right[i]))

print("Total 1: " + str(total1))

# Part 2

total2 = 0
for i in range(len(left)):
    total2 += (left[i] * right.count(left[i]))

print("Total 2: " + str(total2))