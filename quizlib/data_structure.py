import os
__author__ = 'Eugene'


def init():
    number_of_classes = 0
    if not os.path.exists("../data"):
        os.chdir("..")
        os.mkdir("data")
        os.chdir("data")

        while True:
            try:
                number_of_classes = int(input("Please enter the number of classes that you would like to create: "))
                break
            except ValueError:
                print("Please ensure that you enter a number. Please try again.")

        for class_id in range(0, number_of_classes):
            class_teacher_name = input("Please input the class teacher's name for class {}: ".format(class_id))
            os.mkdir("{0} - {1}".format(class_id, class_teacher_name))

    else:
        print("Initial file setup has already been run. If you want to reset all data, delete the data folder.")

    os.chdir("../quizlib")
