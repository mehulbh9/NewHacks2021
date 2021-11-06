from assignment import Assignment
from course import Course
from day import Day
from exam import Exam

def makeDay(name):
    day = Day(name)
    return day

def checkIntandPass(str, output):
    temp = 0
    try:
        temp = int(str)
        output = temp
        return True
    except ValueError:
        print("Error: invalid input")
        return False
    


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
            output = 0
            dateFound = False
            for day in daysOfTheWeek:
                if (commandList[1] == day.name()):
                    dateFound = True
                    if (checkIntandPass(commandList[2], output)):
                        if (output >= 0 and output <= 24):
                            day.timeTotal = output
                        else:
                            print("Error: hour has to be between 0 and 24")
                    else:
                        print("Error: invalid input")
            if (not dateFound):
                print("Error: invalid day")
                
        elif (keyword == "print"): #print
            pass
        elif (keyword == "exit"):
            exit = True
    

if __name__ == "__main__":
    main()
