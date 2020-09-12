import csv
import json

filepointer = open('sample_hrm.csv')
csvfile = csv.reader(filepointer, delimiter=",")
data = {}

# skip one row -- just skip the header
next(csvfile)
for row in csvfile:
    employee = {
        'id': row[0],
        'first_name': row[1],
        'last_name': row[2],
        'title': row[3],
        'salary': row[4]
    }
    data[row[0]] = employee

print(data)