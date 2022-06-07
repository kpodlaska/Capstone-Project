import logging
import argparse
import configparser
import uuid
import os
import random
import json
import ast
f_name = "test.json"
d_schema = "{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\",\"age\": \"int:rand(1, 90)\"}"
schema_dict=ast.literal_eval(d_schema.strip())
schema_dict2=json.loads(d_schema)

print(type(schema_dict), schema_dict.keys(), schema_dict.values())
print(type(schema_dict2), schema_dict2.keys(), schema_dict2.values())