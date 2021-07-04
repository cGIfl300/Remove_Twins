#!/usr/bin/python
from pathlib import Path
import argparse

# Create a class Remove_twins
class Remove_twins:
    ''' Removing twin files.
    nosize: Boolean if true, ignore filesizes
    '''
    def __init__(self, nosize = False):
        self.filenames = []  # filenames list
        self.path = Path(".")  # define default path for futur functionnalities...
        self.nosize = nosize
        if self.nosize:
            print("nosize")
        self.__list_files()

    def __list_files(self):
        self.filenames = list(self.path.glob("*"))
        # Remove directories
        for filename in self.filenames:
            if not filename.is_file():
                self.filenames.remove(filename)

    def __remove_ext(self, filename):
        """Return the filename with no extention

        Keyword arguments:
        filename -- the original filename
        """
        # Check if a .something exist in the actual filename
        if filename.rfind(".") == -1:
            return filename

        return filename[:filename.rfind(".")-1]

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
            file1_noext = self.__remove_ext(str(file1))
            file2_noext = self.__remove_ext(str(file2))
            # Test if the filenames are similar
            if (
                file2_noext[0 : len(file1_noext)] == file1_noext
                and (file1.stat().st_size == file2.stat().st_size
                or self.nosize)
            ):
                files_to_remove.append(file2)
            if (
                file1_noext[0 : len(file2_noext)] == file2_noext
                and (file1.stat().st_size == file2.stat().st_size
                or self.nosize)
            ):
                files_to_remove.append(file1)

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
    parser.add_argument(
        "--nosize", help="ignoring filesizes", action="store_true"
    )
    args = parser.parse_args()

    # Instance the main Class
    hereIam = Remove_twins(nosize = args.nosize)

    if args.dry:
        print("Running dry test.")
        hereIam.dry()
        exit(0)

    print("Removing twins from this directory...")
    hereIam.remove()
