import os
from quizlib import student
from quizlib import quizlib_directory
__author__ = 'Eugene'


class Class:
    def __init__(self, class_id, teacher_name=None, new=False):

        self.class_id = class_id
        self.student_list = []
        if new:  # If it's a new class, then create the file before running any other methods on it
            self.teacher_name = teacher_name
            self.create_class_file()
        self.teacher_name = self.get_class_teacher()
        self.update_class_object()

    def update_class_object(self):  # Refresh object data from files

        os.chdir(self.get_class_directory(self.class_id))

        for student_save_filename in os.listdir(os.getcwd()):
            student_save_filename = student_save_filename.strip(".txt")
            temp_student_save_filename_list = student_save_filename.split(" - ")
            student_id = temp_student_save_filename_list[0]
            name = temp_student_save_filename_list[2]
            self.student_list.append(student.Student(student_id, self.class_id, name))

        os.chdir(quizlib_directory)

    def create_new_student(self, student_name):  # Creates new student object - file creation handled by student class
        student_object = student.Student(len(self.student_list), self.class_id, student_name, True)
        self.student_list.append(student_object)  # Add the student object to the class list

    def create_class_file(self):  # Creates new class directory
        from quizlib import data_directory
        print("Creating new folder for class {}...".format(self.class_id))
        print(data_directory)
        os.chdir(data_directory)
        os.mkdir("{0} - {1}".format(self.class_id, self.teacher_name))
        os.chdir(quizlib_directory)

    def get_class_teacher(self):
        directory = self.get_class_directory(self.class_id)
        return directory.split(" - ")[1]

    def get_class_scores_alphabetical(self):  # All sorting functions defined below will follow a similar pattern
        def alphabetical_sort_key(list_item):  # Define a sort key
            return list_item[1]

        scores_list = []  # Create a list of objects to be sorted
        for student_object in self.student_list:
            scores_list.append([student_object.get_student_best_score(), student_object.student_name])

        scores_list = sorted(scores_list, key=alphabetical_sort_key)  # Sort the list
        return scores_list

    def get_class_scores_descending(self):
        def top_scores_sort_key(list_item):
                return list_item[0]

        scores_list = []
        for student_object in self.student_list:
            for score in student_object.student_scores:
                scores_list.append([score, student_object.student_name])

        scores_list = sorted(scores_list, key=top_scores_sort_key, reverse=True)
        return scores_list

    def get_class_average_scores_descending(self):
        def averages_sort_key(list_item):
            return list_item[0]

        scores_list = []
        for student_object in self.student_list:
            scores_list.append([student_object.get_student_average_score(), student_object.student_name])

        scores_list = sorted(scores_list, key=averages_sort_key, reverse=True)
        return scores_list

    def get_class_directory(self, class_id):
        from quizlib import data_directory
        os.chdir(data_directory)
        for directory in os.listdir(os.getcwd()):
            if str(class_id) == directory.split(" - ")[0]:
                return directory
