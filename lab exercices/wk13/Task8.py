from Task8_open import File


def main():
    print("I am using a class to open a text file and print it if I find it only.")
    documentTXT = File()
    print("Example: Task8.txt or task8.txt (Found), Task-8.txt or task-8.txt (not Found), Task-8 or task-8 (file does not end with 'txt')")
    file_name = input("What is the name of the file that you want to open: ")
    documentTXT.validate_file(file_name)


if __name__ == "__main__":
    main()
