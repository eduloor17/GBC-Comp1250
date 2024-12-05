#Task7-Checking if the letter is vowel
letter = input("Enter Only one letter (could be lower or upper case): ")
# Convert the letter to lowercase to handle uppercase input
letter = letter.lower()
# Determine if the letter is a vowel
if letter in ['a', 'e', 'i', 'o', 'u']:
    print(f"The letter '{letter}' is a vowel.")
else:
    print(f"Please try again. '{letter}' is not a vowel.")
