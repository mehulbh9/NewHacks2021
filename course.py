class Course:
    name = ""
    priority = 2
    difficulty = 1

    def __init__(self, name):
        self.name = name
        self.assignments = []
        self.exams = []

    def __init__(self, name, priority, difficulty):
        self.name = name 
        self.priority = priority
        self.difficulty = difficulty 
        self.assignments = []
        self.exams = []




    def __str__(self) -> str:
        string = "Course " + str(self.name) + "\n\n"
        string += "Priority : " + str(self.priority) + "\n"
        string += "Difficulty : " + str(self.difficulty) + "\n" 
        string += "\nUpcoming assignments : " + "\n"
        for assignment in self.assignments: 
            name = assignment.name.split("%")[1]
            string += str(name) + ": due " + str(assignment.duedate.strftime("%a")) + ", " + str(assignment.duedate.strftime("%B")) + " " + str(assignment.duedate.strftime("%d")) + ", " + str(assignment.duedate.strftime("%Y")) + " and completion time : " + str(getTimeInHours(assignment.time)) + "\n"
        string += "\nUpcoming exams : " + "\n"
        for exam in self.exams: 
            name = exam.name.split("%")[1]
            string += str(name) + " with weight " + str(exam.weight) + "% on " + str(exam.date.strftime("%a")) + ", " + str(exam.date.strftime("%B")) + " " + str(exam.date.strftime("%d")) + ", " + str(exam.date.strftime("%Y")) + " and estimated study time : " + str(getTimeInHours(exam.study_time)) + "\n"
        return string

def getTimeInHours(timeInMinutes):
    result = ""
    hour = int(int(timeInMinutes) / 60)
    minutes = int(timeInMinutes) % 60
    if (hour > 0):
        result += str(hour)
        if (hour == 1):
            result += " hour "
        else : 
            result += " hours "
    if (minutes > 0):
        result += str(minutes)
        if (minutes == 1):
            result += " minute"
        else:
            result += " minutes"
    return result

