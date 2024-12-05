names = []
# For loop to get 3 names into names
for i in range(1, 4):
    f_name = input(f"Enter the name N. {i}: ")
    names.append(f_name)
#print variable names as a list
print(names)
# Converting from list to a tuple
names_tuple = tuple(names)
print(names_tuple)