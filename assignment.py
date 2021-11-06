import datetime

class Assignment:

    name = ""
    duedate = datetime.datetime(1,1,1)

    def __init__(self, name, due_date):
        self.name = name
        self.duedate = due_date

        
    
