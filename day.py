class Day:
    name = ""
    timeTotal = 0
    timeWork = 0
    timeFree = 0
    targetTime = 0.0
    

    def __init__(self, dayofweek):
        self.name = dayofweek
        self.assignments = []

    
    def __str__(self) -> str:
        string = self.name.ljust(10)+ "-> has "+ str(len(self.assignments))+ " assignments planned, with "+ str(self.timeWork) + " minutes of work and "+str(self.timeFree)+" minutes free."
        if (len(self.assignments)>0):
            string += "\nThe assignments are:\n"
            for asm in self.assignments:
                string += str(asm.split('%')[1])+" from "+ str(asm.split('%')[0] + "\n")
        return string
    
    def setTotal(self, time):
        if (time >= 0 and time <= 1440):
            self.timeTotal = time
        else:
            print("Error: minute has to be between 0 and 1440")
    
    def appendAsm(self, name):
        self.assignments.append(name)
