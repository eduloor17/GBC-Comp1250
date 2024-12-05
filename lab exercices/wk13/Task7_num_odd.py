import sys


class Odd:
    def __init__(self):
        self.number = None

    def validate_and_check_odd(self, user_input):
        try:
            user_number = int(user_input)
            self.is_odd_num(user_number)
        except ValueError:
            print(f"Error: '{user_input}' is not a valid number!", file=sys.stderr)

    @staticmethod
    def is_odd_num(number):
        try:
            # Check if the number is Odd or not.
            if number % 2 == 0:
                raise ValueError("The number is not odd.")
            # Display the number
            print(f"Odd Number: {number}")
        except ValueError as e:
            # Display an error message if the input is invalid or not odd
            print(f"Error: {e}", file=sys.stderr)
