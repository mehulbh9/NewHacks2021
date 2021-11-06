import datetime

class Exam:
    name = ""
    weight = 0
    study_time = 0
    date = None

    def __init__(self, name, weight, study_time, date):
        self.name = name
        self.weight = weight
        self.study_time = study_time
        self.date = date
