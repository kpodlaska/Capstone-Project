import path
import unittest
data_schema = '{“date”:”timestamp:”, “name”: “str:rand”, “type”:”[‘client’, ‘partner’, ‘government’]”, ' \
              '“age”: “int:rand(1, 90)”} '

fake_dict = path.create_fake_dict(data_schema)
def test_keys_values(fake_dict):
    assert True

def test_dict_len_matches_key_number(fake_dict):
    assert True

def test_dictionary_len(fake_dict):
    assert True

def test_result_data_type(fake_dict):
    assert True
# if you have idea how the test should look like let me know
#we can check if result is dict
#if len(keys*) keys is equal len(values*) *potential (only then we can create dict

print(fake_dict)
