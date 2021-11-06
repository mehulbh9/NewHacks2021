class Day:
    name = ""
    timeTotal = 0
    timeWork = 0
    timeFree = 0
    

    def __init__(self, dayofweek, timeTotal):
        self.name = dayofweek
        self.timeTotal = timeTotal
