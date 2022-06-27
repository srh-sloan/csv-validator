import csv
import os


def validate_csv_file(expected_cols, expected_digits, csv_path):
    print(os.path.dirname(os.path.abspath(__file__)))
    print('validating csv at', csv_path)
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 0;
        valid = True
        for row in csv_reader:
            print('\t',row)
            row_count+=1
            if len(row) > 1:
                print('\tRow',row_count,'has >',expected_cols,'columns:',row)
                valid = False
                break
    return valid


