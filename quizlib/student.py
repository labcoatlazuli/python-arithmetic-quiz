import os, statistics
from quizlib import quizlib_directory
from quizlib import get_class_directory
__author__ = 'Eugene'


class Student:
    def __init__(self, student_id, class_id, student_name, new=False):
        self.student_id = student_id
        self.class_id = class_id
        self.student_name = student_name
        self.student_scores = []
        if new == True:
            self.create_student_file()
        self.update_student_object_scores()

    def update_student_object_scores(self):

        os.chdir(get_class_directory(self.class_id))
        filename = "{0} - {1} - {2}.txt".format(self.student_id, self.class_id, self.student_name)

        with open(filename, "r") as f:
            self.student_scores = list(f)
            for score in self.student_scores:
                score = score.strip("\n")

            self.student_scores = [int(score) for score in self.student_scores]

        os.chdir(quizlib_directory)

    def create_student_file(self):
        os.chdir(get_class_directory(self.class_id))
        filename = "{0} - {1} - {2}.txt".format(self.student_id, self.class_id, self.student_name)
        with open(filename, "x"):
            print("{} has been created successfully.".format(filename))

        os.chdir(quizlib_directory)
        self.update_student_object_scores()

    def update_student_savefile(self, new_score):
        os.chdir(get_class_directory(self.class_id))
        filename = "{0} - {1} - {2}.txt".format(self.student_id, self.class_id, self.student_name)

        score_list = []
        with open(filename, "r") as f:
            score_list = list(f)

        if len(score_list) >= 3:
            with open(filename, "w") as f:
                f.write(score_list[len(score_list) - 1])
                f.write(score_list[len(score_list) - 2])

        with open(filename, "a") as f:
            f.write("{}\n".format(new_score))

        os.chdir(quizlib_directory)
        self.update_student_object_scores()

    def get_student_best_score(self):
        if len(self.student_scores) == 0:
            return None
        else:
            return max(self.student_scores)

    def get_student_average_score(self):
        if len(self.student_scores) == 0:
            return 0
        else:
            return statistics.mean(self.student_scores)
