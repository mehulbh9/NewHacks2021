class Course:
    name = ""
    priority = 0
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
        string += "Priority: " + str(self.priority) + "\n"
        string += "Difficulty: " + str(self.difficulty) + "\n"
        string += "Upcoming assignments : " + "\n"
        for assignment in self.assignments: 
            string += assignment.name + " with due date " + str(assignment.duedate.strftime("%a")) + ", " + str(assignment.duedate.strftime("%B")) + " " + str(assignment.duedate.strftime("%d")) + ", " + str(assignment.duedate.strftime("%Y")) + " and completion time : " + assignment.time + "\n"
        string += "Upcoming exams : " + "\n"
        for exam in self.exams: 
            string += exam.name + " on " + str(exam.date.strftime("%a")) + ", " + str(exam.date.strftime("%B")) + " " + str(exam.date.strftime("%d")) + ", " + str(exam.date.strftime("%Y")) + " and estimated study time : " + exam.study_time + "\n"
        return string
