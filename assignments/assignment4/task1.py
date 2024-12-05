import os
import sys


class FilenameClass:
    def __init__(self):
        self.filename = ""
        self.content = ""

    def get_filename(self):
        # Step 1: Ask the user for a filename
        self.filename = input("Enter a filename (task1.csv or task1): ")

        # Step 1a: Check if the filename has an extension
        if '.' not in self.filename:
            print(f"Adding the extension 'txt' because the file '{self.filename}' does not have '.' character.")
            # Step 1ai: Add a ".txt" extension if not present
            self.filename += '.txt'
        elif not self.filename.endswith('.txt') and '.' not in self.filename.split('/')[-1]:
            # Only add .txt if there's no other extension and not if the user enters a directory path
            self.filename += '.txt'

        # Step 1b: Check if the filename already exists in the current working directory
        if os.path.isfile(self.filename):
            # Step 1bi: Raise an exception if the file already exists
            raise FileExistsError(f"The file '{self.filename}' already exists. Please choose a different name.")

    def create_file(self):
        # Step 2: Create a file with the given name
        with open(self.filename, 'w') as file:
            pass  # File is created

    def get_content(self):
        # Step 3: Ask the user for content
        self.content = input("Enter content for the file: ")

        # Step 3a: Ensure that the content is at least 10 characters
        if len(self.content) < 10:
            # This file is going to delete if the content is less than 10 characters.
            os.remove(self.filename)
            print(f"{self.filename} has been deleted because the content is less than 10 characters.")

            # Step 3ai: Raise an exception if content is less than 10 characters
            raise ValueError("Content must be at least 10 characters long.")

    def append_content_to_file(self):
        # Step 4: Append the data to the file with a newline character at the end
        with open(self.filename, 'a') as file:
            file.write(self.content + '\n')

    def main(self):
        try:
            self.get_filename()
            self.create_file()
            self.get_content()
            self.append_content_to_file()
            print(f"Content has been written to {self.filename}")
        except Exception as e:
            print(f"There is an ERROR. Check here for more Detail: {e}", file=sys.stderr)


# Run the FileManager
if __name__ == "__main__":
    filename_class = FilenameClass()
    filename_class.main()
