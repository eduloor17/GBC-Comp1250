"""
Assignment 3 File

Full Name: Eduardo Loor
Student Number: 101503932

Please complete the functions based on their definitions and examples
"""


def how_many_vowels(text):
    """
    This function counts the number of vowels in a text. Vowels are the characters a,e,i,o,u and are case insensitive

    >>> how_many_vowels("ABC")
    1
    >>> how_many_vowels("aEiO")
    4
    >>> how_many_vowels("TRY")
    0
    >>> how_many_vowels("First Question")
    5
    """
    # This part will check how many vowels are in a text, and then add to count variable.
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1

    return count


def count_whitespaces(spaces):
    """
    This function counts the number of whitespaces in a text.

    >>> count_whitespaces("  \t ")  # remember, a tab is 4 white spaces
    6
    >>> count_whitespaces(" Hello World ")
    3
    >>> count_whitespaces("#PythonRules")
    0
    >>> count_whitespaces(" ")
    1
    """
    # if there is a space in spaces variable, I will use the variable count to know how many spaces
    count = 0
    for char in spaces:
        if char.isspace():
            count += 1
    return count


def odd_or_even(number):
    """
    This function determines either
    a) if the numerical value is odd or even
    b) if the number of characters of a string is odd or even
    c) if the number of elements in a list or tuple is add or even
    d) If any other data type, there is no return

    >>> odd_or_even("hello world")
    'odd'
    >>> odd_or_even(1234)
    'even'
    >>> odd_or_even(12.34)
    'even'
    >>> odd_or_even(list(range(2, 11)))
    'odd'
    >>> odd_or_even(tuple("cool"))
    'even'
    """
    # I will check if the number is odd or even for int, and float types.
    if isinstance(number, (int, float)):
        if int(number) % 2 == 0:
            return 'even'
        else:
            return 'odd'
    #I will check if the number are string, list or tuples, and also if the length of number is even or odd
    elif isinstance(number, (str, list, tuple)):

        if len(number) % 2 != 0:
            return 'odd'
        else:
            return 'even'
    else:
        # For different types, I do not return anything.
        return None


def extract_letters(unique):
    """
    Extract all the UNIQUE letters present in the text string.

    >>> extract_letters("Python 123 is C00!_")
    ('p', 'y', 't', 'h', 'o', 'n', 'i', 's', 'c')
    >>> extract_letters("Numbers Are Overrated!")
    ('n', 'u', 'm', 'b', 'e', 'r', 's', 'a', 'o', 'v', 't', 'd')
    >>> extract_letters("123 456")
    ()
    >>> extract_letters("|3 E N!C3")
    ('e', 'n', 'c')
    """
    # I will use the following variables for separate letters to have
    # no repeated letters, and without special characters
    letters = []
    repeat = set()
    # I use this Loop to verify that each character in the text is unique
    for char in unique:
        if char.isalpha():
            # If there a letter between A to Z, I will make lower case (a to z)
            lower_char = char.lower()
            if lower_char not in repeat:
                repeat.add(lower_char)
                letters.append(lower_char)
    return tuple(letters)


def extract_numbers(extract):
    """
    Extract all the numerical digits in a text string.
    Allow duplicate values as digits.
    Sort the digits in reverse order

    >>> extract_numbers("Python 15-4 is C00!_")
    [5, 4, 1, 0, 0]
    >>> extract_numbers("Sample Param")
    []
    >>> extract_numbers("122333")
    [3, 3, 3, 2, 2, 1]
    >>> extract_numbers("I won 1st prize out of 482 contestants")
    [8, 4, 2, 1]
    >>> extract_numbers("My mom Ana has 65, and I have 40 years")
    [6, 5, 4, 0]
    >>> extract_numbers("My sister has 2 Sons. I would like to have 1 daughter")
    [2, 1]

    Add 2 more Doctests (EDTEST, I did.)
    """
    digits = [int(char) for char in extract if char.isdigit()]
    return sorted(digits, reverse=True)


def sum_of_odd_numbers(*total):
    """
    Write a function that returns the sum of odd numbers
    The function accepts an unlimited about of numerical values
    Assume that there will only be numerical values passed to the function

    Add the necessary parameters to the function definition
    Add a description of the param value
    Add a description of the return value

    >>> sum_of_odd_numbers(1, 3, 5)
    9
    >>> sum_of_odd_numbers(1, 1, 2, 2, 3, 3, 4, 5, 6)
    13
    >>> sum_of_odd_numbers(2, 4, 6, 8, 0, 1)
    1
    >>> sum_of_odd_numbers(1, 2, 3, 4, 5, 6, 7)
    16
    >>> sum_of_odd_numbers(5, 6, 7, 8, 9, 10, 11)
    32
    >>> sum_of_odd_numbers(100, 201, 333, 402, 530, 600, 708)
    534

    Add 2 more Doctests (EDTEST, I did.)
    """
    # I use sum_of_numbers to count only odd number, so I ask if the num % 2 != 0
    # if I want the sum of even, I could change num % 2 == 0
    sum_of_numbers = sum(num for num in total if num % 2 != 0)
    # I return the sum_of_numbers after perform the addition operation.
    return sum_of_numbers


def remove_vowels(no_vowel, except_case=()):
    """
    This function removes all the vowels in a text and returns a new text without any vowels.
    Vowels are the characters a,e,i,o,u and are case insensitive
    This function allows an optionally tuple data type parameter that represents a series of vowels to except in extraction


    >>> remove_vowels("I like applies")
    ' lk ppls'

    >>> remove_vowels("PYTHON is SUPER cOOl")
    'PYTHN s SPR cl'

    >>> remove_vowels("Are you having fun?", ('a', 'u'))
    'Ar yu havng fun?'

    >>> remove_vowels("Why oh why?", ('o', 'i'))
    'Why oh why?'

    >>> remove_vowels("George Brown College is here for you", ('e'))
    'Gerge Brwn Cllege s here fr y'

    >>> remove_vowels("Do you have Smarter TV?", ('a', 'u'))
    'D yu hav Smartr TV?'

    # I will remove all o vowels in my sentence include LaLo (My nickname), other vowels is allowed!
    >>> remove_vowels("The only way that LaLo can learn is PRACTICE", ('a', 'e', 'i', 'u'))
    'The nly way that LaL can learn is PRACTICE'

    Add 2 more Doctests (EDTEST, I did.)
    """

    # Define the vowels to remove
    vowels = "aeiou"
    # Create a set of vowels to be excluded from removal
    except_set = set(vowel.lower() for vowel in except_case)

    # Remove vowels from text except those in the except_set
    remove_it = ''.join(char for char in no_vowel if char.lower() not in vowels or char.lower() in except_set)

    return remove_it
