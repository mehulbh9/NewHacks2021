import datetime

class Assignment:

    name = ""
    duedate = datetime(0,0,0)

    def __init__(self, name, due_date):
        self.name = name
        self.duedate = due_date

        
    
