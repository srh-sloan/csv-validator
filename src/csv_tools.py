import csv
import os

class Csv_Validator:


    def __init__(self, expected_cols, expected_digits):
        self.errors = []
        self.output = []
        self.total_rows = 0
        self.expected_cols = expected_cols
        self.expected_digits = expected_digits
        self.any_errors = False
        

    def validate_csv_file(self, csv_path):
        self.errors.append(f"validating csv at {csv_path.path}")
        self.output.append(f"validating csv at {csv_path.path}")
        valid = True
        
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            row_count = 0;
            for row in csv_reader:
                #print('\t',row)
                row_count+=1

                # Check if we have the expectd number of columns in this row
                if len(row) != self.expected_cols:
                    self.errors.append(f"\tRow {row_count} has {len(row)} columns:{row} (expected: {self.expected_cols})")
                    valid = False

                # Check format
                if valid == True:
                    col_count = 0
                    for col in row:
                        col_count += 1

                        # Check for number of digits
                        if len(col) != self.expected_digits:
                            self.errors.append(f"\tRow {row_count} column {col_count} has {len(col)} digits:' {col} (expected: {self.expected_digits})")
                            valid = False

                        # Check is numeric    
                        if not col.isnumeric():
                            self.errors.append(f"\tRow {row_count} column {col_count} contains non-numeric characters: {row}")
                            valid = False

        # If row_count is 0, it was empty
        if row_count == 0:
            valid = False
            self.errors.append(f"\tInvalid: no rows")
        self.output.append(f"\t{csv_path.name} was valid: {valid}, rows: {row_count} \n")
        self.total_rows += row_count
        if not valid:
            self.any_errors = True
        return valid

    def print_results(self, output_folder):
        print('\nERRORS\n')
        print(self.errors)
        print('\n\nOutput\n')
        print(self.output)
        print('\n\nTotal Rows:',self.total_rows)

        if output_folder:
            with open(output_folder + "/output.txt", 'w') as out_file:
                for line in self.output:
                    out_file.write(line + "\n")
                out_file.write(f"\n\nTotal Rows: {self.total_rows}")
                out_file.write(f"\nAny errors? {self.any_errors}")
            with open(output_folder + "/errors.txt", 'w') as out_file:
                for line in self.errors:
                    out_file.write(line + "\n")


    def validate_in_folder(self, csv_path):
        valid = self.validate_csv_file(csv_path)
        self.print_results
        return valid


    def find_files_in_dir(self,root_dir):
        with os.scandir(root_dir) as iter:
            for entry in iter:
                print(entry)
                if entry.is_dir():
                    with os.scandir(entry) as iter2:
                        for entry2 in iter2:
                            print("\t",entry2)
                            if entry2.is_dir():
                                with os.scandir(entry2) as iter3:
                                    for entry3 in iter3:
                                        print("\t\t",entry3)
                                        if entry3.is_file() and entry3.name.endswith(".csv"):
                                            print("\t\tis a csv")
                                            self.validate_csv_file(entry3)
        self.print_results(root_dir)