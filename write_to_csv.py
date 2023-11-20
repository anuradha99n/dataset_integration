import csv
def write_to_csv(output_file, files_and_data):
    try:
        with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['Data_ID'] + list(files_and_data[0][1].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for file_data in files_and_data:
                row_data = {'Data_ID': file_data[0], **file_data[1]}
                writer.writerow(row_data)
                print(f"{file_data[0]} : Done")
                
    except PermissionError:
        print(f"Permission error: {output_file}")
    except FileNotFoundError:
        print(f"File not found: {output_file}")
    except UnicodeDecodeError:
        print(f"Unicode encode error in file: {output_file}")
    except csv.Error as e:
        print(f"CSV error in file: {output_file}")
