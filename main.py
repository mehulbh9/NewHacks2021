from assignment import Assignment
from course import Course
from day import Day
from exam import Exam

def makeDay(name):
    day = Day(name)
    return day

def checkInt(str):
    temp = 0
    try:
        temp = int(str)
        return temp
    except ValueError:
        print("Error: invalid input")
        return 0
    


def main():
    namesOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    daysOfTheWeek = []

    for name in namesOfTheWeek:
        daysOfTheWeek.append(makeDay(name))

    while(True):
        command = input()
        commandList = command.split();
        keyword = commandList[0]
        
        if (True): #course
            
        elif (True): #assignment
            
        elif(True): #time
            
        elif (True): #print
            
    

if __name__ == "__main__":
    main()
