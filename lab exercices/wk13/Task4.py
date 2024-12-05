import os


def main():
    # Create a sub-directory (task4 folder) in the current working directory
    folder = "task4"
    os.makedirs(name=folder, exist_ok=True)
    print(f"The sub-directory {folder} folder is created.")


if __name__ == "__main__":
    main()
