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

object_01 = script_01_check_exported_data()

path = "/media/raheel/22687D06687CD9CD/projects/groundowl-app/appData/"
path2 = "/media/raheel/22687D06687CD9CD/projects/groundowl-app/appState/groundowl-canbus/app_state.json"
texts = ["mock_geophex_v2_raw_emi", "mock_geophex_v2_raw_gps", "mock_ml_model_v1_till_depth", "IDSGPRMock"]
text_01 = "mock_geophex_v2_raw_emi"
text_02 = "mock_geophex_v2_raw_gps"
text_03 = "mock_ml_model_v1_till_depth"
text_04 = "IDSGPRMock"

print(text_01, object_01.is_data_exported(path, text_01))
print(text_02, object_01.is_data_exported(path, text_02))
print(text_03, object_01.is_data_exported(path, text_03))
print(text_04, object_01.is_data_exported(path, text_04))

if (object_01.is_data_exported(path, text_01)) and (object_01.is_data_exported(path, text_02)) and (
        object_01.is_data_exported(path, text_03)) and (object_01.is_data_exported(path, text_04)):
    print("Exported data is verified!")
    object_01.delete_all__exported_date(path)
    print("Deleted all export data!")

else:
    print("Exported data is not verified!")
    object_01.delete_all__exported_date(path)
    print("Deleted all export data!")

#os.remove("/media/raheel/22687D06687CD9CD/projects/groundowl-app/appState/groundowl-canbus/app_state.json")
