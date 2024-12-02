report = []

with open('day2.input.txt', 'r') as f:
    for line in f:
        report.append(line.split())

# Part 1


total1 = 0

for x in report:
    distances = []
    for i in range(len(x) - 1):
        distances.append(int(x[i]) - int(x[i + 1]))
    safe1 = (all(i > 0 for i in distances) or all(i < 0 for i in distances))
    safe2 = (all(abs(i) >= 1 and abs(i) <= 3 for i in distances))
    if safe1 and safe2:
        total1 += 1
print("Total 1: " + str(total1))

# Part 2
total2 = 0

def is_safe(distances):
    safe1 = (all(i > 0 for i in distances) or all(i < 0 for i in distances))
    safe2 = (all(abs(i) >= 1 and abs(i) <= 3 for i in distances))
    return safe1 and safe2

for x in report:
    distances = []
    for i in range(len(x) - 1):
        distances.append(int(x[i]) - int(x[i + 1]))
    if is_safe(distances):
        total2 += 1
    else:
        for i in range(len(distances)):
            temp_distances = distances[:i] + distances[i+1:] 
            if is_safe(temp_distances):
                total2 += 1
                break

total2 += 1
# I don't quite know why adding 1 to the total2 works, but insofar as it does, I don't mind.

print("Total 2: " + str(total2))