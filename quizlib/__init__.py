import os
__author__ = 'Eugene'

"""This file here is run automatically before anything else"""
quizlib_directory = os.getcwd()
# data_directory = ""


#  if __name__ != "__main__":
print("Checking for existing data...")
from quizlib import data_structure
if not os.path.exists("../data"):
    os.chdir("..")
    os.mkdir("data")
    os.chdir("data")
    data_directory = os.getcwd()
    print("Data folder at: {}".format(data_directory))
    data_structure.create_new_classes([], True)
    print()

else:
    os.chdir("../data")
    data_directory = os.getcwd()
    print("Data folder at: {}".format(data_directory))
    print("Initial file setup has already been run. If you want to reset all data, delete the data folder.")
    print()

os.chdir("../quizlib")

def get_class_directory(class_id):
        os.chdir(data_directory)
        for directory in os.listdir(os.getcwd()):
            if str(class_id) == directory.split(" - ")[0]:
                return directory
