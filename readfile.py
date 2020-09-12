# open the file for the reading
filename = input("please provide filename: ")
filepointer = open(filename)
for line in filepointer:
    print(line.strip())