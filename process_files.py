import os
from read_csv import read_text_file
from scrap_web import scrap_data

def process_files_in_folder(folder_path):
    files_and_data = []
    for filename in os.listdir(folder_path):
        # If your file Names are in different format change the below line (".txt") 
        # Accepted formats are txt,csv only
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            data_dict = read_text_file(file_path)
            if data_dict == 0:
                continue
            sample_id = filename.split('-')[0] 
            bpd_stage = scrap_data(sample_id) # Scrap bpd stages from the site
            files_and_data.append((sample_id, data_dict, bpd_stage))
    return files_and_data