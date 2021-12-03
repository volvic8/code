import os

for folder_path, sub_folder, sub_file in os.walk(".\\data\\test_data"):
    for file in sub_file:
        print(folder_path + "\\" + file)
