#Task3-Finding character in a name variable
name = input("Enter your name: ")
char = input("Enter a character: ")
position = name.lower().find(char.lower())
if position != -1:
    print(f"The character: '{char}' in the name: '{name}' is found at position '{position}'.")
    print(True)
else:
    print(False)
