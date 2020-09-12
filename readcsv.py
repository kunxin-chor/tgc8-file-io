import csv

filepointer = open('sample_hrm.csv')
csvfile = csv.reader(filepointer, delimiter=",")
# skip one row -- just skip the header
next(csvfile)
for row in csvfile:
    print("ID: ", row[0])
    print("First name: ", row[1])
    print("Last name: ", row[2])
    print("Title: ", row[3])
    print("Salary: ", row[4])
    print()
