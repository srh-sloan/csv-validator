import csv_tools as tools
import os

def test_csv_valid():
    print(os.path.dirname(os.path.abspath(__file__)))
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/test-data/3/1/5.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == True

def test_csv_invalid_columns_all():
    print(os.path.dirname(os.path.abspath(__file__)))
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/invalid-data/multi-column.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == False


def test_csv_invalid_columns_some():
    print(os.path.dirname(os.path.abspath(__file__)))
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/invalid-data/some-multi-column.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == False
