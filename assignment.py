import datetime

class Assignment:

    name = ""
    duedate = None
    time = 0 #minutes

    def __init__(self, name, due_date, time):
        self.name = name
        self.duedate = due_date
        self.time = time

    def getDay(self):
        day = int(self.duedate.strftime("%j"))
        if (day <= 120):
            day += 366
        return day

    
