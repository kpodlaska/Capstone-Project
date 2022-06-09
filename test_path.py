import path

data_schema = '{“date”:”timestamp:”, “name”: “str:rand”, “type”:”[‘client’, ‘partner’, ‘government’]”, ' \
              '“age”: “int:rand(1, 90)”} '

fake_dict = path.create_fake_dict(data_schema)
# if you have idea how the test should look like let me know
print(fake_dict)
