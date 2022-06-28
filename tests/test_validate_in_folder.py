from csv_tools import Csv_Validator

def test_scan_dir():
    validator = Csv_Validator(1,12)
    root_dir_path = "/home/srhsloan/test-workspace/csv-validator/tests/test-data/"
    validator.find_files_in_dir(root_dir_path)
