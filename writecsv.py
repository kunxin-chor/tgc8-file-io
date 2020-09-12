import csv

# use the with block to close the filepointer when we are done
filename = input("Enter filename: ")
# when pythone exists the code in the with block for any reason, filepointer will close
with open(filename, 'w') as filepointer:
    csv_writer = csv.writer(filepointer)

    csv_writer.writerow(["Food", "Price", "Ingredients"])
    csv_writer.writerow(["Chicken rice", "2.50", "chicken and rice"])
    csv_writer.writerow(["Pancake", "1.50", "milk and dough"])
    csv_writer.writerow(["Fish fillet", "5.00", "fish and dough"])
