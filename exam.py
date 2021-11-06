class Exam:
    weight = 0
    importance = 0
    studyTime = 0
    course = ""
    day = None
    def __init__(self, weight, importance, study_time, course, day):
        self.weight = weight
        self.importance = importance
        self.studyTime = study_time
        self.day = day
        self.course = course
