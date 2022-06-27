import csv_tools as tools
import os

def test_csv_valid():
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/test-data/3/1/5.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == True

def test_csv_invalid_columns_all():
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/invalid-data/multi-column.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == False


def test_csv_invalid_columns_some():
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/invalid-data/some-multi-column.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == False

def test_csv_invalid_empty_sheet():
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/invalid-data/empty.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == False


def test_csv_invalid_empty_row():
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/invalid-data/empty-field.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == False

def test_csv_invalid_bad_ids_length():
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/invalid-data/invalid-length.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == False

def test_csv_invalid_bad_ids_chars():
    csv_path = '/home/srhsloan/test-workspace/csv-validator/tests/invalid-data/invalid-chars.csv'
    
    assert tools.validate_csv_file(1,12, csv_path) == False