filepointer = open("numbers.txt")
total = 0
for line in filepointer:
    total += int(line)
print("The total is", total)