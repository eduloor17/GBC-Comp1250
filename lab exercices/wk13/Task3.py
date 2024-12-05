import os


def main():
    # Store all the files and folders of the current working directory
    entries = os.listdir()

    # Output each file/directory on a new line
    for entry in entries:
        print(entry)


if __name__ == "__main__":
    main()
