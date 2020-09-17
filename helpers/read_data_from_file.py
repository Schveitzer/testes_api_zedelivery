import json


def read_test_data_from_json(path):
    with open('base-files/' + path) as test_data:
        test_data = json.load(test_data)
    return test_data


def read_test_data_from_json_tuple(path):
    test_data = read_test_data_from_json(path)
    test_data = [tuple(row) for row in test_data]
    return test_data
