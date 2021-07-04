#!/usr/bin/python
from pathlib import Path
import argparse

# Create a class Remove_twins
class Remove_twins:
    def __init__(self):
        self.filenames = []  # filenames list
        self.path = Path(".")  # define default path for futur functionnalities...
        self.__list_files()

    def __list_files(self):
        self.filenames = list(self.path.glob("*"))
        # Remove directories
        for filename in self.filenames:
            if not filename.is_file():
                self.filenames.remove(filename)

    def __files_to_remove(self):
        files_to_remove = []
        # Get the filenames to delete
        file1 = 0
        file2 = 0
        # If there is less than 2 files, we have nothing to do
        if len(self.filenames) < 2:
            print("Nothing to do when less than 2 files.")
            return []
        # Order filenames by alphabetical names
        hereIam.filenames.sort()
        # Now we list the files to remove
        for i in range(len(self.filenames) - 1):
            file1 = self.filenames[i]
            file2 = self.filenames[i + 1]
            # Test if the filenames are similar
            if (
                str(file2)[0 : len(f"{file1}")] == f"{file1}"
                and file1.stat().st_size == file2.stat().st_size
                or str(file1)[0 : len(f"{file2}")] == f"{file2}"
                and file1.stat().st_size == file2.stat().st_size
            ):
                files_to_remove.append(file2)
        return files_to_remove

    def dry(self):
        files_to_remove = self.__files_to_remove()
        print(files_to_remove)

    def remove(self):
        files_to_remove = self.__files_to_remove()
        for filename in files_to_remove:
            print(f"Removing {filename}")
            filename.unlink()


if __name__ == "__main__":
    # Add arguments managment
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dry", help="dry test, not deleting anything", action="store_true"
    )
    args = parser.parse_args()

    # Instance the main Class
    hereIam = Remove_twins()

    if args.dry:
        print("Running dry test.")
        hereIam.dry()
        exit(0)

    print("Removing twins from this directory...")
    hereIam.remove()
