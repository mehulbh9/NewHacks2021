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
        string = "The course "+ self.name+ " has priority "+ self.priority+ " and difficulty "+ self.difficulty + "."
        return string
