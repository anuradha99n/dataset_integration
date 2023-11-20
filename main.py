# Example usage:
from read_csv import read_text_file
from list_files import list_files_in_folder

# Example usage:
folder_path = "data_files"
files = list_files_in_folder(folder_path)

for file in files:
    data = read_text_file(f'{folder_path}/{file}')
    print(data)
    print("==========")


# file_path = "./data_files/GSM3425978-tbl-1.txt"
# result_dict = read_text_file(file_path)

# # Print the resulting dictionary
# for key, value in result_dict.items():
#     print(f"{key}: {value}")