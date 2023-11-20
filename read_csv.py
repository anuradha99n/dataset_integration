import csv

def read_text_file(file_path):
    data_dict = {}
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) == 2:
                data_dict[row[0]] = row[1]
    return data_dict

# # Example usage:
# file_path = "GSM3425979-tbl-1.txt"
# result_dict = read_text_file(file_path)

# # Print the resulting dictionary
# for key, value in result_dict.items():
#     print(f"{key}: {value}")
