from assignment import Assignment
from course import Course
from day import Day
from exam import Exam

def makeDay(name):
    day = Day(name)
    return day

def main():
    namesOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    daysOfTheWeek = []

    for name in namesOfTheWeek:
        daysOfTheWeek.append(makeDay(name))

    while(True):
        command = input()
        keyword = command.split()[0]
        
        if (True): #course
            pass
        elif (True): #assignment
            pass
        elif(True): #time
            pass
        elif (True): #print
            pass
    

if __name__ == "__main__":
    main()
