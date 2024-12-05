import sys


class File:
    def __init__(self):
        self.filename = None

    @staticmethod
    def validate_file(filename):
        try:
            # Check if the file name ends with ".txt"
            if not filename.endswith(".txt"):
                raise NameError("The file name does not end with '.txt'.")

            # Try to open and output the file contents
            with open(filename, 'r') as file:
                contents = file.read()
                print(contents)

        except NameError as e:
            # Handle NameError
            print(f"Error: {e}", file=sys.stderr)

        except FileNotFoundError:
            # Handle FileNotFoundError
            print("Error: File not found.", file=sys.stderr)
