start = int(input("Enter the start number: "))
last = int(input("Enter the last number: "))
increment = int(input("Enter the increment number: "))
print("Output while loop1: ")
i1 = 0
while i1 < start:
    print(i1, end=" ")
    i1 = i1 + 1
print("\nOutput while loop2: ")
i2 = 1
while i2 < start:
    print(i2, end=" ")
    i2 = i2 + 1
print("\nOutput while loop3: ")
i3 = start
while i3 < last:
    print(i3, end=" ")
    i3 = i3+1
print("\nOutput while loop4: ")
i4 = start
while i4 < last:
    print(i4, end=" ")
    i4 = i4 + int(increment)