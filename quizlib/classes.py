import os
from quizlib import student
from quizlib import quizlib_directory, get_class_directory
__author__ = 'Eugene'


class Class:
    def __init__(self, class_id):

        self.class_id = class_id
        self.student_list = []
        self.update_class_object()

    def update_class_object(self):

        os.chdir(get_class_directory(self.class_id))

        for student_save_filename in os.listdir(os.getcwd()):
            student_save_filename = student_save_filename.strip(".txt")
            temp_student_save_filename_list = student_save_filename.split(" - ")
            student_id = temp_student_save_filename_list[0]
            name = temp_student_save_filename_list[2]
            self.student_list.append(student.Student(student_id, self.class_id, name))

        os.chdir(quizlib_directory)

    def create_new_class_student_object(self, student_name):
        pass

    def get_class_teacher(self):
        directory = get_class_directory(self.class_id)
        return directory.split(" - ")[1]