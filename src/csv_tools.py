import csv

class Csv_Validator:


    def __init__(self, expected_cols, expected_digits):
        self.errors = []
        self.output = []
        self.total_rows = 0
        self.expected_cols = expected_cols
        self.expected_digits = expected_digits
        

    def validate_csv_file(self, csv_path):
        self.errors.append(f"validating csv at {csv_path}")
        self.output.append(f"validating csv at {csv_path}")
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
        self.output.append(f"CSV at {csv_path} was valid: {valid} \n")
        self.total_rows += row_count
        return valid

    def print_results(self):
        print('\nERRORS\n')
        print(self.errors)
        print('\n\nOutput\n')
        print(self.output)
        print('\n\nTotal Rows:',self.total_rows)


    def validate_in_folder(self, csv_path):
        valid = self.validate_csv_file(csv_path)
        self.print_results
        return valid
