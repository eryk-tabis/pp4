class Course:
    def __init__(self):
        self.students_list = []

    def add_student(self, student):
        if len(self.students_list) < 10:
            self.students_list.append(student)
            print(f"{student} has been enrolled in the course.")
        else:
            raise Exception("The course is already full. Enrollment is closed.")
