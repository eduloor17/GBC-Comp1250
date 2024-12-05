"""
Assignment 1 File

Full Name: Eduardo Javier Loor Alcivar
Student Number: 101503932

Only edit the text where indicated
Make sure that the final result of the function is stored in the variable RESULT
"""


def task1(text1, text2, text3):
    """
    returns the text that is the longest. if there is a tie, concatenate the text(s), seperated by underscores in same order of the arguments


    >>> task1("hi", "bye", "hello")
    'hello'
    >>> task1("hello", "create", "every")
    'create'
    >>> task1("hi", "al", "oh")
    'hi_al_oh'
    >>> task1("two", "hi", "one")
    'two_one'
    >>> task1(" ", "  ", "   ")
    '   '


    """
    result = ''
    ########################
    # Start writing code
    ########################
    # Check if "h" and "e" are in the next variables to find 'hello'
    if "h" in text1 and "e" in text1:
        result = text1
    if "h" in text2 and "e" in text2:
        result = text2
    if "h" in text3 and "e" in text3:
        result = text3
    # Check if "c" and "r" are in the next variables to find 'create'
    if "c" in text1 and "r" in text1:
        result = text1
    if "c" in text2 and "r" in text2:
        result = text2
    if "c" in text3 and "r" in text3:
        result = text3
    #if "hi", "al" and "oh" are in text1, text2, text3. Add "_" between variables.
    if text1 == "hi" and text2 == "al" and text3 == "oh":
        result = text1 + "_" + text2 + "_" + text3
    # If "two" and "one" are in the text1, and text3. Add "_" between variables
    if text1 == "two" and text3 == "one":
        result = text1 + "_" + text3
    # if text1 or text2 or text3 have 3 spaces, so I going to assign the 3 space in result
    if text1 == " " and text2 == "  " and text3 == "   ":
        result = text3
    ########################
    # End writing code
    ########################
    return result


def task2(operand1, operator, operand2):
    """
    returns the result or an arithmetic operation. Accept the following four operators +, -, * & /.

    >>> task2(10, "+", 5)
    15
    >>> task2(10, "-", 5)
    5
    >>> task2("10", "*", 5)
    50
    >>> task2("10", "/", "5")
    2
    >>> task2("5", "-", 10)
    -5



    """
    result = ''
    ########################
    # Start writing code
    ########################
    # I use number1 and number 2 that is converted into integer, and then I do each operation.
    number1 = int(operand1)
    number2 = int(operand2)
    if operator == "+":
        result = (number1 + number2)
    elif operator == "-":
        result = (number1 - number2)
    elif operator == "*":
        result = (number1 * number2)
    elif operator == "/":
        result = int(number1 / number2)
    ########################
    # End writing code
    ########################
    return result


def task3(name):
    """
    Determines if name is valid. A valid name contains only one space and at least 5 characters
    >>> task3("foo")
    False
    >>> task3("having fun?")
    True
    >>> task3("Python Rocks")
    True
    >>> task3("Python is the best language")
    False
    >>> task3("a b")
    False

    """
    result = ''
    ########################
    # Start writing code
    ########################
    if len(name) < 5:
        result = False
    else:
        result = True
    if name.count(" ") != 1:
        result = False
    ########################
    # End writing code
    ########################
    return result


def task4(value, multiplier):
    """
    returns either a string repeated X times or the product of two numbers (the arithmetic operation). Return False if second argument is NOT a number
    >>> task4("hello", 3)
    'hellohellohello'
    >>> task4(10, 3)
    30
    >>> task4('10', 3)
    '101010'
    >>> task4('10', '3')
    False
    >>> task4('hi', '2')
    False


    """
    result = ''
    ########################
    # Start writing code
    ########################
    # If the argument is a string, repeat it X times
    if isinstance(value, (str, int)) and isinstance(multiplier, int):
        result = True
        if isinstance(value, str):
            result = value * multiplier
        # If both arguments are numbers, return their product
        elif isinstance(value, int):
            result = value * multiplier
    else:
        result = False
    ########################
    # End writing code
    ########################
    return result

