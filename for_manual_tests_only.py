import logging

import creating_fake_data
def create_data_without_output_file(lines):
    if lines > 0:
        for i in range(lines):
            data = creating_fake_data.create_fake_dict(parsed_args.data_schema)
            print(f"{data}")
    else:
        logging.critical("You can't process with this number of lines")
create_data_without_output_file(7)
