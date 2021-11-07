class Day:
    name = ""
    timeTotal = 0
    timeWork = 0
    timeFree = 0
    targetTime = 0.0
    assignments = []

    def __init__(self, dayofweek):
        self.name = dayofweek

    def __str__(self) -> str:
        string = self.name, "has", str(len(self.assignments)), "assignments planned, with", str(self.timeWork), "minutes of work and",str(self.timeFree),"minutes free. \n"
        string += "The assignments are:\n"
        for asm in self.assignments():
            string += (asm.name().split('%'))[0],"from",(asm.name().split('%'))[1]
        return string
    
    def setTotal(self, time):
        if (time >= 0 and time <= 1440):
            self.timeTotal = time
        else:
            print("Error: minute has to be between 0 and 1440")
