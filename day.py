class Day:
    name = ""
    timeTotal = 0
    timeWork = 0
    timeFree = 0
    targetWork = 0.0
    

    def __init__(self, dayofweek):
        self.name = dayofweek

    def __str__(self) -> str:
        string = self.name + " has " + str(self.timeWork).rjust(4) + " minutes of work, " + str(self.timeFree).rjust(4) + " minutes of free. and " + str(self.timeFree).rjust(4) + "minutes Free."
        return string
    
    def setTotal(self, time):
        if (time >= 0 and time <= 1440):
            self.timeTotal = time
        else:
            print("Error: minute has to be between 0 and 1440")
