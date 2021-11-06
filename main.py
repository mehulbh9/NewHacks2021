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
    exit = False

    for name in namesOfTheWeek:
        daysOfTheWeek.append(makeDay(name))

    while(not exit):
        command = input()
        commandList = command.split()
        keyword = commandList[0]
        
        
        if (keyword == "course"): #course
            pass
        elif (keyword == "assignment"): #assignment
            pass
        elif(keyword == "time"): #time
            pass
        elif (keyword == "print"): #print
            pass
        elif (keyword == "exit"):
            exit = True
    

if __name__ == "__main__":
    main()
