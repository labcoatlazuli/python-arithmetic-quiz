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

    def create_new_student(self, student_name):
        student_object = student.Student(len(self.student_list), self.class_id, student_name, True)
        self.student_list.append(student_object)

    def get_class_teacher(self):
        directory = get_class_directory(self.class_id)
        return directory.split(" - ")[1]

    def get_class_scores_alphabetical(self):
        def alphabetical_sort_key(list_item):
            return list_item[1]

        scores_list = []
        for student_object in self.student_list:
            scores_list.append([student_object.get_student_best_score(), student_object.student_name])

        scores_list = sorted(scores_list, key=alphabetical_sort_key)
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
