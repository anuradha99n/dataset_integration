import os
from read_csv import read_text_file

def process_files_in_folder(folder_path):
    files_and_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            data_dict = read_text_file(file_path)
            data_id = filename.split('-')[0]
            files_and_data.append((data_id, data_dict))
    return files_and_data