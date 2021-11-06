import datetime

class Exam:
    weight = 0
    study_time = 0
    date = datetime(0,0,0)

    def __init__(self, weight, study_time, date):
        self.weight = weight
        self.study_time = study_time
        self.date = date
