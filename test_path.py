import json
import unittest
import main


class TestDictionary(unittest.TestCase):
    def test_dict_len_matches_key_number(self):
        data_schema = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\"," \
                      "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": " \
                      "\"int:rand(1, 6)\"} "
        dict_given = main.create_fake_dict(data_schema)
        dict_values = dict_given.values()
        dict_keys = dict_given.keys()
        self.assertEqual(len(dict_values), len(dict_keys))

    def test_add_lines_to_file(self):
        file_name = "magic_file_generator.json"
        d_schema = "{\"date\": \"timestamp:\"} "
        path = "/Users/kpodlaska/Desktop"
        f_line_given = 10
        file_given = main.create_output_file(f_line_given, d_schema, path, file_name)
        print(file_given)
        f = open(file_given)
        data = json.load(f)
        f.close()
        self.assertEqual(f_line_given, len(data))

    def test_creating_number_of_files(self):
        pass

    def test_data_types(self):
        pass
    #want to check create_fake_data.py
    #It's a must according to Capstone specification

    def test_clear_path(self):
        pass
    #doesn't exist yet

    def test_data_schema_loaded_in_json(self):
        pass
    #todo: have to use fixtures

    def save_file_on_disc(self):
        pass
    #
        # if you have idea how the test should look like let me know
#we can check if result is dict
#if len(keys*) keys is equal len(values*) *potential (only then we can create dict



if __name__ == '__main__':
    unittest.main()