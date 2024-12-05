import os


def create_file(path, filename):
    with open(os.path.join(path, filename), 'w') as f:
        pass  # Create an empty file


def main():
    # Create the sub_directories folders
    sub_directories = "d1/d2/d3"
    os.makedirs(name=sub_directories, exist_ok=True)

    # Define file names
    files = [
        "d1/projectComp3105.pdf", "d1/study-notes.docx",
        "d1/d2/CiscoBasicConfiguration.txt", "d1/d2/index.html",
        "d1/d2/d3/friend.jpg", "d1/d2/d3/tennis-video.mp4"
    ]

    # Create files in each directory
    for file in files:
        create_file(os.path.dirname(file), os.path.basename(file))

    print(f"Directories {sub_directories} and files created.")


if __name__ == "__main__":
    main()
