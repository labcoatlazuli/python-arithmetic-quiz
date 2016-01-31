import os
from quizlib import quizlib_directory, data_directory
__author__ = 'Eugene'

class_object_list = []
student_id = 0
class_id = 0



def update_all():

    global class_object_list, class_id
    class_object_list = []  # Clear class object list ready for refresh
    from quizlib import classes
    os.chdir(data_directory)

    for directory in os.listdir(os.getcwd()):
        class_id = directory.split(" - ")[0]
        class_object_list.append(classes.Class(class_id))

    os.chdir(quizlib_directory)



class InvalidSelectionError(Exception):
    pass

while True:
    update_all()


    print("Hello! Welcome to the quiz menu! Please enter a number to perform a task.")
    print("1: Play the quiz. You will be asked to login beforehand.")
    print("2: View scores for a class")
    print("3: Add new classes")
    print("4: Add new student accounts")
    choice = input("Please enter your choice here: ")
    if choice == "1":

        print("Just before you play, you'll need to login.")
        # Please enter class here.
        print("Here's a list of all the registered classes. Please enter the ID of your class.")
        for class_object in class_object_list:
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

        if input("Do you know your student ID? Yes/no: ").lower() not in ["y", "yes"]:
            potential_student_list = []
            student_name = input("Please enter your name, we'll show you a list of matching students: ")
            for student_object in class_object_list[class_id].student_list:
                if student_name in student_object.student_name:
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

        from quizlib import quiz
        student_score = quiz.quiz()
        class_object_list[class_id].student_list[student_id].update_student_savefile(student_score)

    elif choice == "2":
        print("Here's a list of all the registered classes. Please enter the ID of your class.")
        for class_object in class_object_list:
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

        print("Now you have three options. Please enter the number of your choice of sorting method:")
        print("1: By students in alphabetical order, showing each student's top score")
        print("2: By each individual score, highest to lowest")
        print("3: By the average score, highest to lowest")
        sorting_method = input("Your choice: ")

        if sorting_method == "1":
            def alphabetical_sort_key(item):
                return item.student_name
            sorted_student_object_list = []
            sorted_student_object_list = sorted(class_object_list[class_id].student_list, key=alphabetical_sort_key)
            for student in sorted_student_object_list:
                print("{0}, top score of {1}".format(student.student_name, student.get_student_best_score()))

        elif sorting_method == "2":
            def top_scores_sort_key(list_item):
                return list_item[0]
            scores_list = []
            for student in class_object_list[class_id].student_list:
                for score in student.student_scores:
                    scores_list.append([score, student.student_name])

            scores_list = sorted(scores_list, key=top_scores_sort_key, reverse=True)
            if len(scores_list) == 0:
                print("This class hasn't had any scores yet.")
            else:
                for score_item in scores_list:
                    print("Score of {0} achieved by {1}".format(score_item[0], score_item[1]))

        else:
            print("Invalid choice.")

    elif choice == "3":
        pass
    elif choice == "4":
        pass

    else:
        print("Please enter a valid choice.")

    print()