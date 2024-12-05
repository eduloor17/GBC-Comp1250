#Task 6-Ask the user for a text-Ask the user for a number
#-Typecast the number into an integer-Output both the text and number using string formatting
print('Task 6')
text = input("Enter your name: ")
number = input("Please enter a number: ")
number = int(number)
print(f"{text}, your lucky number is: {number}")