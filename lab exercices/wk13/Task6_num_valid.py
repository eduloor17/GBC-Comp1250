import sys


class Number:
    def __init__(self):
        self.number = None

    def is_number_valid(self, user_number):
        try:
            self.number = float(user_number)
            print(f"You entered the number: {self.number}")
        except ValueError:
            print("Invalid number entered.", file=sys.stderr)
