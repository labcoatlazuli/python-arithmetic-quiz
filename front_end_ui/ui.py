import os
from quizlib import quizlib_directory, data_directory
__author__ = 'Eugene'

class_object_list = []
student_id = 0
class_id = 0


def update_all(): # Updates all objects from save files

    global class_object_list, class_id
    class_object_list = []  # Clear class object list ready for refresh

    from quizlib import classes
    os.chdir(data_directory)

    for directory in os.listdir(os.getcwd()): # Creates class objects from class folders
        class_id = directory.split(" - ")[0] # Gets class id from the class folder file path
        class_object_list.append(classes.Class(class_id)) # Adds new class object to list

    max_id = 0
    for class_obj in class_object_list: # Find highest class id
        if int(class_obj.class_id) > int(max_id):
            max_id = class_obj.class_id

    temp_list = []
    for count in range(int(max_id) + 1): # This entire section moves class objects to the list index specified by their
        class_object_present = False     # class id, so if there are missing class folders for eg class 3, index 3
        for class_obj in class_object_list: # is not taken up by another class. Instead a placeholder None is assigned.
            if int(class_obj.class_id) == count:
                temp_list.append(class_obj)
                class_object_present = True
                break
        if class_object_present == False:
            temp_list.append(None)

    class_object_list = temp_list.copy()
    del temp_list


    os.chdir(quizlib_directory) # Always return to the starting directory after file handling operations

def select_class_id(): # General class selector function: prints out current classes, prompts for a selection
    print("Here's a list of all the registered classes. Please enter the ID of your class.")

    global class_id, class_object_list # We are modifying variables outside the scope of the function w/ global keyword
    for class_object in class_object_list:
        if class_object is not None:
            print(" - {0}'s class, class ID {1}".format(class_object.get_class_teacher(), class_object.class_id))
    while True:
        try:
            try:
                class_id = int(input("Your class ID: "))
            except ValueError:
                raise InvalidSelectionError

            if class_id not in range(len(class_object_list)):
                raise InvalidSelectionError
            break
        except InvalidSelectionError:
            print("Please enter a valid Class ID.")


class InvalidSelectionError(Exception):
    pass

while True:
    update_all() # Update class objects from save files at the beginning of each program loop

    print("Hello! Welcome to the quiz menu! Please enter a number to perform a task.")
    print("1: Play the quiz. You will be asked to login beforehand.")
    print("2: View scores for a class")
    print("3: Add new classes")
    print("4: Add new student accounts")

    choice = input("Please enter your choice here: ") # choice is left as a string - no need for ValueError try-catch
    if choice == "1":

        print("Just before you play, you'll need to login.")

        select_class_id()
        current_class = class_object_list[class_id]

        if input("Do you know your student ID? Yes/no: ").lower() not in ["y", "yes"]: # Name search function
            potential_student_list = []
            student_name = input("Please enter your name, we'll show you a list of matching students: ").lower()
            for student_object in current_class.student_list:
                if student_name in student_object.student_name.lower():
                    potential_student_list.append(student_object)

            if len(potential_student_list) == 0:
                print("Name not found. Please try again, or ask the teacher to create an account for you.")
                continue

            else:
                for student in potential_student_list:
                    print("{0}, Student ID {1}".format(student.student_name, student.student_id))

        while True:  # Check that the answer is a valid number
            try:
                try:
                    student_id = int(input("Your Student ID: "))

                except ValueError:
                    raise InvalidSelectionError

                break
            except InvalidSelectionError:
                print("Please enter a valid Student ID.")

        if student_id not in range(len(class_object_list[class_id].student_list)):
            print("Student ID not found. Try the name search, otherwise ask your teacher to create an account for you.")
            continue

        current_student = current_class.student_list[student_id]

        from quizlib import quiz
        student_score = quiz.quiz() # Runs the quiz after login
        current_student.update_student_savefile(student_score) # Update save files

    elif choice == "2": # Returns scores. See classes.py for sorting methods
        select_class_id()

        current_class = class_object_list[class_id]

        print("Now you have three options. Please enter the number of your choice of sorting method:")
        print("1: By students in alphabetical order, showing each student's top score")
        print("2: By each individual score, highest to lowest")
        print("3: By the average score, highest to lowest")
        sorting_method = input("Your choice: ")

        if sorting_method == "1":
            scores_list = current_class.get_class_scores_alphabetical()
            if len(scores_list) == 0:
                print("This class hasn't had any scores yet.")

            else:
                for score_item in scores_list:
                    print("{1}, top score of {0}".format(score_item[0], score_item[1]))

        elif sorting_method == "2":
            scores_list = current_class.get_class_scores_descending()
            if len(scores_list) == 0:
                print("This class hasn't had any scores yet.")

            else:
                for score_item in scores_list:
                    print("Score of {0} achieved by {1}".format(score_item[0], score_item[1]))

        elif sorting_method == "3":
            scores_list = current_class.get_class_average_scores_descending()
            if len(scores_list) == 0:
                print("This class hasn't had any scores yet.")

            else:
                for score_item in scores_list:
                    print("Average score of {0} achieved by {1}".format(score_item[0], score_item[1]))

        else:
            print("Invalid choice.")

    elif choice == "3": # Creates new classes on request. See data_structure.py
        os.chdir(data_directory)
        from quizlib import data_structure
        data_structure.create_new_classes(class_object_list)

    elif choice == "4": # Creates new students on request. See data_structure.py
        select_class_id()
        current_class = class_object_list[class_id]
        from quizlib import data_structure
        data_structure.create_new_students(current_class)

    else:
        print("Please enter a valid choice.")

    print()
