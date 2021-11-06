from day import Day

def makeDay(name):
    day = Day(name)
    return day

daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for name in daysOfTheWeek:
    makeDay(name)
    

