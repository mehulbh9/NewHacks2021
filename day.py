class Day:
    name = ""
    timeTotal = 0
    timeWork = 0
    timeFree = 0
    

    def __init__(self, dayofweek):
        self.name = dayofweek

    def __str__(self) -> str:
        print ("The day", self.name, "has", self.timeTotal, "minutes free,", self.timeWork, "minutes of work, and", self.timeFree, "minutes Free.")