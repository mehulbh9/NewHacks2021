class Day:
    name = ""
    timeTotal = 0
    timeWork = 0
    timeFree = 0
    

    def __init__(self, dayofweek):
        self.name = dayofweek

    def __str__(self) -> str:
        print (self.name, "has", str(self.timeWork).rjust(4), "minutes of work,", str(self.timeFree).rjust(4), "minutes of free. and", str(self.timeFree).rjust(4), "minutes Free.")