Capstone Project
In Capstone project you can generate output json file with schema you want.
Use console to put arguments:
- path_to_save_files - You can define path for output file
- files_count        - You can define how many json file do you want to generate. Default value is 1. If you choose 0 result will be printed on screen.
- file_name          - You can choose name to your file. Default value is fake_data_file. (Necessary if files_count more than 0)
- file_prefix        - You can choose {count,random,uuid}. Default is count. Define file name with prefix for multiple files.
- data_schema        - You can provide data Schema  for your output files. Default is data_schema = {"date": "timestamp:","name": "str:rand","type": "["client", "partner",
                        "government"]","animal_type": "["cat", "dog", "monkey,"tiger"]","age": "int:rand(1, 90)","kids_number": "int:rand(1, 6)"}
- data_lines         - You can choose how many lines your output file has. Default is 100
- multiprocessing    - You can choose The number of processes used to create files. Default is 5.
- clear_path         - You can choose if you want to clear directory before you create files
