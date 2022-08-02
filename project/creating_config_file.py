import configparser
import os

ABSOLUTE_PATH = os.path.dirname(os.path.abspath("main.py"))


def create_config_ini():
    config = configparser.ConfigParser()
    results_dir = str(os.path.join(ABSOLUTE_PATH, "results"))



    config['DEFAULT'] = {'path_to_save_files': results_dir,
                         'files_count': '1',
                         'file_name': 'fake_data_file',
                         'file_prefix': 'count',
                         'data_schema': "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": "
                                        "\"['client', 'partner', 'government']\","
                                        "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": "
                                        "\"int:rand(1, 90)\",\"kids_number\": "
                                        "\"int:rand(1, 6)\"} ",
                                        'data_lines': '100',
                                        'multiprocessing': '5'}
    config_file_path = str(os.path.join(ABSOLUTE_PATH, "project/","default.ini"))
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    #print((os.path.join(absolute_path, "results")))
    create_config_ini()

