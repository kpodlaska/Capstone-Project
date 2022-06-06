
# Python program to explain os.getcwd() method

# importing os module
import os
import uuid

# Get the current working
# directory (CWD)


"""
def existing_dir(prospective_dir):
    isdir = os.path.isdir(args.path_to_save_files)
    try:
        isdir
        return prospective_dir
    except TypeError:
        print("Check the path one more time")
        logging.critical("DIR not exsist!!")


existing_dir("/Castone")


if args.path_to_save_files==".":
    path = os.getcwd()
    logging.debug("You are in current directory. Path :".format(path))
else:
    path=existing_dir(args.path_to_save_files)
    logging.debug("Path :", format(path))
#cos tu nie dziala"""
lista=[]
for i in range(4):
    x_i=uuid.uuid4()
    lista.append(x_i)
    print(x_i)
print(lista)
print(lista[0])
