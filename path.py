import logging
import argparse
import configparser
import uuid
import os
import random

def construct_files(file_name, prefix, how_many_files):
    ext="json"
    prefixes = []
    if prefix == "count":
        for n in range(how_many_files):
            prefixes.append(str(n+1))
    elif prefix == "random":
        for n in range(how_many_files):
            number=random.randint(1,1_000_000_000_000)
            prefixes.append(number)
    elif prefix == "uuid":
        for n in range(how_many_files):
            x_n = uuid.uuid4()
            prefixes.append(x_n)

    full_filenames = []
    for prefix_ in prefixes:
        full_filename = file_name+"_" + str(prefix_) + "."+ext
        full_filenames.append(full_filename)

    return full_filenames

y=construct_files("super","count", 4)
print("test 1",y)
y=construct_files("super","count", 100)
print("test 2",y)
y=construct_files("super","count", -7)
print("test 3",y)
y=construct_files("super", "uuid", 90)
print("test 4",y)
y=construct_files("super", "uuid", 30)
print("test 5",y)
y=construct_files("super", "uuid", 37)
print("test 6",y)
y=construct_files("super", "random", 37)
print("test 7",y)
