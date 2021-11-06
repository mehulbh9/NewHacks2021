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
        string = "The course "+ str(self.name)+ " has priority "+ str(self.priority)+ " and difficulty "+ str(self.difficulty) + "."
        return string
