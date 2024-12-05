# This program is going to create a csv file and store 4 data type in a row of 4 (3x4)
import csv

student = [
    ["eduloor17", " Eduardo ", "  Loor  ", 40],
    ["lucky7777", " Luciano ", "  Lopez ", 29],
    ["cissy1991", " Cissy   ", "  Chou  ", 33]
]

with open("task3.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "Firstname", "Lastname", "Age"])
    writer.writerows(student)

print(f"Student was written successfully. Student List: {student}")
