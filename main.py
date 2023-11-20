from process_files import process_files_in_folder
from write_to_csv import write_to_csv

folder_path = "data_files"
data_dict = process_files_in_folder(folder_path)

output_file = "output.csv"

files_and_data = process_files_in_folder(folder_path)
write_to_csv(output_file, files_and_data)
