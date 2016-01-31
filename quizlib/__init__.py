from pathlib import Path
import os
__author__ = 'Eugene'

quizlib_directory = os.getcwd()

if __name__ != "__main__":
    print("Checking for existing data...")
    from quizlib import data_structure
    data_structure.init()

os.chdir("../data")
data_directory = os.getcwd()
os.chdir(quizlib_directory)


def get_class_directory(class_id):
        os.chdir(data_directory)
        for directory in os.listdir(os.getcwd()):
            if str(class_id) == directory.split(" - ")[0]:
                return directory