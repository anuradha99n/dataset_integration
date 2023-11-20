import csv

def read_text_file(file_path):
    data_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                if len(row) == 2:
                    data_dict[row[0]] = row[1]
        return data_dict
    except FileNotFoundError:
        print(f"File not Found: {file_path}")
    except PermissionError:
        print(f"Permission error: {file_path}")
    except UnicodeDecodeError:
        print(f"Unicode decode error in file: {file_path}")
    except csv.Error as e:
        print(f"CSV error in file: {file_path}, {e}")
    return 0


