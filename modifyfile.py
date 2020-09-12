filename = input("Enter filename: ")
filepointer = open(filename, 'r')
# read each line into the list
lines = list(filepointer)

line_no = int(input("Which line to delete?"))
del lines[line_no]

filepointer.close()

filepointer = open(filename, 'w')
for l in lines:
    filepointer.write(l)
filepointer.close()