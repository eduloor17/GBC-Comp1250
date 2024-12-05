start = int(input("Enter the start number: "))
last = int(input("Enter the last number: "))
increment = int(input("Enter the increment number: "))
#print(start, last, increment)
print("Output 1: ")
for i1 in range(0, start):
    print(i1, end=" ")
print("\nOutput 2: ")
for i2 in range(1, start):
    print(i2, end=" ")
print("\nOutput 3: ")
for i3 in range(start, last):
    print(i3, end=" ")
print("\nOutput 4: ")
for i3 in range(start, last, increment):
    print(i3, end=" ")