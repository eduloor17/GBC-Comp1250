# This program is going to read a file that I created at task1.
#open a file for reading
with open("task1.txt", "r") as file:
    mylist = file.readlines()
    # Write each item of the list to a new line
    for product in mylist:
        print(product.strip())

