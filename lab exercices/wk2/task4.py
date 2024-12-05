#Task 4-Ask the user for 2 numbers
#-Output the sum, product, quotient and difference of the two numbers
num1 = input("Write first number (Ex. 5.5 or 5): ")
num2 = input("Write second number (Ex. 5.5 or 5): ")
num1 = float(num1)
num2 = float(num2)
sum = num1 + num2
diff = num1 - num2
prod = num1*num2
quot = num1/num2
print('Task 4 - Simple calculation')
print(num1, '+', num2, '=',  sum)
print(num1, '-', num2, '=',  diff)
print(num1, '*', num2, '=', prod)
print(num1, '/', num2, '=', quot)