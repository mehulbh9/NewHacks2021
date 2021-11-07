class Course:
    name = ""
    priority = 2
    difficulty = 1
    assignments = []
    exams = []

    def __init__(self, name):
        self.name = name

    def __init__(self, name, priority, difficulty):
        self.name = name 
        self.priority = priority
        self.difficulty = difficulty 


    def __str__(self) -> str:
        string = "Course " + str(self.name) + "\n"
        string += "Priority : " + str(self.priority) + "\n"
        string += "Difficulty : " + str(self.difficulty) + "\n"
        string += "Upcoming assignments : " + "\n"
        for assignment in self.assignments: 
            name = assignment.name.split("&")[1]
            string += str(name) + " with due date " + str(assignment.duedate.strftime("%a")) + ", " + str(assignment.duedate.strftime("%B")) + " " + str(assignment.duedate.strftime("%d")) + ", " + str(assignment.duedate.strftime("%Y")) + " and completion time : " + str(assignment.time) + "\n"
        string += "Upcoming exams : " + "\n"
        for exam in self.exams: 
            name = exam.name.split("&")[1]
            string += str(name) + " on " + str(exam.date.strftime("%a")) + ", " + str(exam.date.strftime("%B")) + " " + str(exam.date.strftime("%d")) + ", " + str(exam.date.strftime("%Y")) + " and estimated study time : " + str(exam.study_time) + "\n"
        string += "\n"
        return string
