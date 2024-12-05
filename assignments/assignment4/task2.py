import os
import sys


class PathFinder:
    def __init__(self):
        self.path = ""

    def get_path(self):
        # Step 1: Ask the user for a path value
        print("If you want to search a folder you can use absolute or relative paths.")
        self.path = input("Enter a directory path for searching: ")

        # Step 1a: Determine if the path exists in the current filesystem
        if not os.path.exists(self.path):
            # Step 1ai: Raise an exception if the path does not exist
            raise FileNotFoundError(f"The path '{self.path}' does not exist. Try Again!!")

    def calculate_totals(self):
        # Initialize counters
        total_items = 0
        total_files = 0
        total_dirs = 0

        # Walk through the directory structure
        for root, dirs, files in os.walk(self.path):
            # Count files and directories
            total_files += len(files)
            total_dirs += len(dirs)
            total_items += len(files) + len(dirs)

        return total_items, total_files, total_dirs

    def main(self):
        try:
            self.get_path()
            total_items, total_files, total_dirs = self.calculate_totals()
            print(f"Total number of files and folders: {total_items}")
            print(f"Total number of files: {total_files}")
            print(f"Total number of directories: {total_dirs}")
        except Exception as e:
            print(f"There is an ERROR. Check here for more Detail: {e}", file=sys.stderr)


# Run the PathManager
if __name__ == "__main__":
    path_finder = PathFinder()
    path_finder.main()
