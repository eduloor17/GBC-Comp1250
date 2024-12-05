# This program is going to create a file with 3 products that are in mylist.
# Define the list of strings
mylist = ["Apple", "Rice", "Milk"]
# Open a file for writing
with open("task1.txt", "w") as file:
    # Write each product of the list to a new line
    for i, product in enumerate(mylist):
        if i < len(mylist) - 1:
            file.write(f"{product}\n")
        else:
            file.write(f"{product}")

print(f"The product at mylist was written successfully. List: {mylist}")
