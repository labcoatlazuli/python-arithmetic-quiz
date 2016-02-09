import os
from quizlib import quizlib_directory, get_class_directory, classes
__author__ = 'Eugene'


"""We're pretty screwed if the user ever wants to delete stuff."""


def init():
    if not os.path.exists("../data"):
        os.chdir("..")
        os.mkdir("data")
        os.chdir("data")

        create_new_classes()

    else:
        print("Initial file setup has already been run. If you want to reset all data, delete the data folder.")

    os.chdir("../quizlib")


def create_new_classes(class_list):
    number_of_new_classes = 0
    empty_class_ids =[]
    for class_obj in class_list:
        if class_obj is None:
            empty_class_ids.append(class_list.index(class_obj))

    if len(empty_class_ids) is not 0:
        print("There are some unused class IDs available.")
        if input("Would you like to fill a few of them first before creating new ones?").lower() in ["y", "yes"]:
            while True:
                try:
                    print("Here are the unused class IDs:")
                    for ID in empty_class_ids:
                        print(ID)
                    positions = input("Please input the unused Class IDs above you would like to fill:")
                    positions = positions.split(",")
                    positions = [int(pos.strip()) for pos in positions]
                    if set(positions).issubset(empty_class_ids):


                except ValueError:
                    pass

    while True:
        try:
            number_of_new_classes = int(input("Please enter the number of classes that you would like to create: "))
            if number_of_new_classes >= 1:
                break
            else:
                print("Please enter a number equal to or larger than 1.")
        except ValueError:
            print("Please ensure that you enter a number. Please try again.")

    number_of_existing_classes = len(os.listdir(os.getcwd()))

    for class_id in range(number_of_existing_classes, number_of_existing_classes + number_of_new_classes):
        class_teacher_name = input("Please input the class teacher's name for class {}: ".format(class_id))

        os.mkdir("{0} - {1}".format(class_id, class_teacher_name))

    os.chdir(quizlib_directory)

def create_new_students(class_object):
    number_of_new_students = 0
    os.chdir(get_class_directory(class_object.class_id))
    while True:
        try:
            number_of_new_students = int(input("Please enter the number of students that you would like to create: "))
            if number_of_new_students >= 1:
                break
            else:
                print("Please enter a number equal to or larger than 1.")
        except ValueError:
            print("Please ensure that you enter a valid number. Please try again.")

    number_of_existing_students = len(os.listdir(os.getcwd()))

    for student_id in range(number_of_existing_students, number_of_existing_students + number_of_new_students):
        student_name = input("Please input the new student's name for new student ID {}: ".format(student_id))
        class_object.create_new_student(student_name)

    os.chdir(quizlib_directory)

def get_highest_id(object_list: list, id_attribute_name: str):
    id_list =[]
    for obj in object_list:
        id_list.append(obj.getattr(id_attribute_name))
    highest_id = max(id_list)
    return highest_id