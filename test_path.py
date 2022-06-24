import creating_fake_data
import unittest
data_schema = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\"," \
           "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": " \
           "\"int:rand(1, 6)\"} "



class TestDictionary(unittest.TestCase):
    def test_dict_len_matches_key_number(self):
        data_schema = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\"," \
                      "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": " \
                      "\"int:rand(1, 6)\"} "
        dict_given = creating_fake_data.create_fake_dict(data_schema)
        dict_values = dict_given.values()
        dict_keys = dict_given.keys()
        self.assertEqual(len(dict_values),len(dict_keys))

    def test_add_lines_to_file(self):
        pass

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