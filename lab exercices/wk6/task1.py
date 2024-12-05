num_A = set(range(10, 21)) # Set A = {10,11,12,13,14,15,16,17,18,19,20}
num_B = set(range(5, 16))  # Set B = {5,6,7,8,9}
num_A_not_num_B = num_A.difference(num_B)
print("Numbers that are only in A but not in B =", num_A_not_num_B)
same_values = num_A.intersection(num_B)
print("Numbers that are repeated in Set A and B:", same_values)
# Printing sets A and B by using for.
print("Values in Set A:")
for A in num_A:
    print(A)
print("Values in Set B:")
for B in num_B:
    print(B)

