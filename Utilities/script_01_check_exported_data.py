import csv
import os
from os import listdir
from os.path import isfile, join


class script_01_check_exported_data:

    def __init__(self):
        pass

    def search_text_in_file(self, search_text: str, file_path: str) -> bool:
        reader = csv.reader(open(file_path, 'r'))
        for row in reader:
            # print(row)
            for column in row:
                if column == search_text:
                    return True

        return False

    def is_data_exported(self, dir_path: str, text: str) -> bool:

        dirs = [join(dir_path, f) for f in listdir(dir_path)]
        # print(dirs)
        all_files = []

        for dir in dirs:
            all_files.append([join(dir, f) for f in listdir(dir) if isfile(join(dir, f))])

        # print(all_files)

        for list_of_file in all_files:
            for file in list_of_file:
                if self.search_text_in_file(search_text=text, file_path=file):
                    return True

        return False

    def delete_all__exported_date(self, dir_path: str) -> None:
        dirs = [join(dir_path, f) for f in listdir(dir_path)]
        all_files = []
        for dir in dirs:
            all_files.append([join(dir, f) for f in listdir(dir) if isfile(join(dir, f))])
        for list_of_file in all_files:
            for file in list_of_file:
                os.remove(file)
        for dir in dirs:
            os.rmdir(dir)
