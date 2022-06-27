import csv
import os


def validate_csv_file(expected_cols, expected_digits, csv_path):
    print('validating csv at', csv_path)
    valid = True
    
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 0;
        for row in csv_reader:
            #print('\t',row)
            row_count+=1
            if len(row) != expected_cols:
                print('\tRow',row_count,'has',len(row),'columns:',row,'(expected: ',expected_cols,')')
                valid = False
            if valid == True:
                col_count = 0
                for col in row:
                    col_count += 1
                    if len(col) != expected_digits:
                        print('\tRow',row_count,'column',col_count, 'has ',len(col),'digits:',col,'(expected: ',expected_digits,')')
                        valid = False
                    if not col.isnumeric():
                        print('\tRow',row_count,'column',col_count, 'contains non-numeric characters:',row)
                        valid = False
    if row_count == 0:
        valid = False
        print('\tInvalid: no rows')
    print('CSV at',csv_path,'was valid:',valid,'\n')
    return valid


