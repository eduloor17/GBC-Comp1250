def function_task1(value1, value2, value3):
    """
    Returns a list of the data types of the arguments as strings.
    Args:
    value1: First argument of any type.
    value2: Second argument of any type.
    value3: Third argument of any type.

    Returns:
    list: A list containing the data types of the arguments as strings.

    doctest:
    # Output: ['str', 'int', 'float']
    >>> function_task1("Ecuador", 40, 3.14)
    ['str', 'int', 'float']

    # Output: ['int', 'float', 'complex']
    >>> function_task1(5, 2.5, 5j)
    ['int', 'float', 'complex']

    # Output: ['str', 'str', 'str']
    >>> function_task1("Argentina", "vs", "Colombia")
    ['str', 'str', 'str']
    """

    # returns a list of the data types of the arguments as strings.
    print([type(value1).__name__, type(value2).__name__, type(value3).__name__])
    #return [type(value1).__name__, type(value2).__name__, type(value3).__name__]

    ##########################
    # End of function_task 1 #
    ##########################

print(f"\033[1m--- Task1 ---\033[0m")
# Call the function with 1 string, 1 integer, and 1 float data type
task1_1 = function_task1("Ecuador", 40, 3.14)
print("Task1_1: 1 string, 1 integer & one float data type", task1_1)  # Output: ['str', 'int', 'float']
# Call the function with all numerical data types
task1_2 = function_task1(5, 2.5, 5j)
print("Task1_2: 1 integer, 1 float & one complex data type", task1_2)  # Output: ['int', 'float', 'complex']
# Call the function with all string data types
print("Final Copa America 2024")
task1_3 = function_task1(value1="Argentina", value2="vs", value3="Colombia")
print("Task1_3: 3 strings data type", task1_3)  # Output: ['str', 'str', 'str']



####################################################################################################

def function_task2(item_name, system_code):
    """
    Repeats the given text a specified number of times if conditions are met.

    Args:
    item_name (str): The string to be repeated.
    system_code (int): The number of times to repeat the string. Must be at least 2.

    Returns:
    str: The repeated string.
    bool: False if the conditions are not met.

    doctest:
    >>> function_task2("Hello", -2)
    False

    >>> function_task2("World", 5)
    'WorldWorldWorldWorldWorld'

    >>> function_task2("Hello", "World")
    False

    >>> function_task2("CANADA", 2)
    'CANADACANADA'
    """

    # Verify the data types of the parameters
    if not isinstance(item_name, str) or not isinstance(system_code, int):
        return False

    # Verify that the system_code has a value of at least 2
    if system_code < 2:
        return False

    # Return item_name repeated N times (system_code)
    return item_name * system_code

    ##########################
    # End of function_task 2 #
    ##########################

# uses of function_task2
print(f"\033[1m--- Task2 ---\033[0m")
print("The Word 'Hello' and the number '-2' will display False. Output:")
task2_1 = function_task2("Hello", -2)
print(task2_1)  # Output: False

print("The Word 'World' and the number '5' will display 5 times the word 'World'. Output:")
task2_2 = function_task2("World", 5)
print(task2_2)  # Output: WorldWorldWorldWorldWorld

print("The Word 'Hello' and the word 'World' will display False. Output:")
task2_3 = function_task2("Hello", "World")
print(task2_3)  # Output: False

print("The Word 'CANADA' and the number '2' will display 2 times the word 'CANADA'. Output:")
task2_4 = function_task2("CANADA", 2)
print(task2_4)  # Output: Task2-Task2-

####################################################################################################

def function_task3():
    """
    Outputs the first name and returns the last name.

    Returns:
    str: The last name.

    doctest:
    >>> function_task3()
    'Loor'
    """
    lastname = "Loor"
    return lastname
    ##########################
    # End of function_task 3 #
    ##########################

print(f"\033[1m--- Task3 ---\033[0m")
print("My first name is:")
#last_name = function_task3()
#print(last_name)
firstname = "Eduardo" #Defining my firstname before function task 3
print(firstname) #Priting my firstname as Global variable

####################################################################################################

def function_task4(num1, num2):
    """
    Determines if the first number is a factor of the second number.

    Args:
    num1 (int): The potential factor.
    num2 (int): The number to be divided.

    Returns:
    bool: True if num1 is a factor of num2, False otherwise.

    doctest:
    >>> function_task4(7, 28)
    True
    >>> function_task4(8, 17)
    False
    """
    return num2 % num1 == 0

    ##########################
    # End of function_task 4 #
    ##########################

#Here two outputs to determinate if the number1 is a factor of number2:
print(f"\033[1m--- Task4 ---\033[0m")
print("The number 7 is a factor of number 28. Output:")
print(function_task4(7, 28))  # Output: True
print("The number 8 is not a factor of number 17. Output:")
print(function_task4(8, 17))  # Output: False

####################################################################################################

import re

def function_task5(postal_code):
    """
    Checks if the given text is a valid Canadian postal code.

    Args:
    postal_code (str): The postal code to validate.

    Returns:
    bool: True if the postal code is valid, False otherwise.

    doctest:
    >>> function_task5("M6G 2H7")
    True
    >>> function_task5("606 2H7")
    False
    """
    matchPS = r"^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$"




    return bool(re.match(matchPS, postal_code))

    ##########################
    # End of function_task 5 #
    ##########################

# Examples of valid and not valid postal code:
print(f"\033[1m--- Task5 ---\033[0m")
print("The postal code is not valid (606 2H7) - Output:")
print(function_task5("606 2H7"))  # Output: False (6 is similar to the letter G and the number 0 is similar to O)
print("The postal code is valid (M6G 2H7) - Output:")
print(function_task5("M6G 2H7"))  # Output: True

####################################################################################################

def function_task6(firstname, lastname):
    """
    Formats the given first and last names into "lastname, firstname".

    Args:
    firstname (str): The first name.
    lastname (str): The last name.

    Returns:
    str: The formatted name.

    doctest:
    >>> function_task6("Eduardo", "Loor")
    'Loor, Eduardo'

    """

    # I ask for name and last name and then I output last name (first), and name (second):

    return f"{lastname}, {firstname}"

    ##########################
    # End of function_task 6 #
    ##########################

print(f"\033[1m--- Task6 ---\033[0m")
print("My lastname, firstname is :")
print(function_task6("Eduardo","Loor"))  # Output: False
