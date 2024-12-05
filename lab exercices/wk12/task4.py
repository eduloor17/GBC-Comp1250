# This program is going to read a csv file that I created at task3
import csv

with open("task3.csv", "r") as file:
    each = csv.reader(file)
    for row in each:
        print("\t".join(row))
