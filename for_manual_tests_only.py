from os import listdir, walk
from os.path import isfile, join

mypath="/Users/kpodlaska/PycharmProjects/pythonProject/Capstone"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)


def existing_dir(prospective_dir):
    isdir = os.path.isdir(prospective_dir)
    try:
        isdir is True
        return prospective_dir
    except TypeError:
        logging.critical("DIR is not exist!")