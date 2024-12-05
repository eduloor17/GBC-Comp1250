#Task6-Determine if the number is positive, negative, or neutral
num = input("Enter a number: ")
num = float(num)
if num > 0:
    print(f"The number {num} is positive.")
elif num < 0:
    print(f"The number {num} is negative.")
else:
    print(f"The number {num} is neutral.")