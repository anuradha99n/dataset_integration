import csv
def write_to_csv(output_file, files_and_data):
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['Data_ID'] + list(files_and_data[0][1].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for file_data in files_and_data:
            row_data = {'Data_ID': file_data[0], **file_data[1]}
            writer.writerow(row_data)