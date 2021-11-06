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
    namesOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #array of names of the week in string
    daysOfTheWeek = [] #array of Day objects
    courses = [] #array of Course objects
    exit = False #whether or not while loop continues

    for name in namesOfTheWeek:
        daysOfTheWeek.append(makeDay(name))

    while(not exit):
        command = input()
        commandList = command.split()
        keyword = commandList[0]
        
        
        if (keyword == "course"): #course
            action = commandList[1]
            if (action == "add"):
                while True:
                    try:
                        name = str(input("What is the name of the course?"))
                        break
                    except ValueError:
                        print("Invalid value. Please enter a string.")
                while True:
                    try: 
                        difficulty = int(input("What would you say the difficulty of the course is out of 5?"))
                    except ValueError:
                        print("Please enter a number between 0 and 5.")
                    
                    if (difficulty < 0 or difficulty > 5):
                        print("Please enter a number between 0 and 5.")
                    else :
                        break
                if (len(courses) == 0):
                    priority = 0; 
                else :
                    print("You currently have the following courses: ")
                    for course in courses: 
                        print (course.name)
                
        elif (keyword == "assignment"): #assignment
            if (commandList[1] == "add"):
                i = 1
                for course in courses:
                    print(i+". "+course.name())
                    i+=1
                while ()
                try:
                    number = int(input("Enter the number of the course"))
                except ValueError:
                    print("Invalid value. Please enter a number between 1 and "+i)


            elif (commandList[1] == "delete"):
                pass
        elif(keyword == "time"): #time
            output = 0
            dateFound = False
            for day in daysOfTheWeek:
                if (commandList[1] == day.name()):
                    dateFound = True
                    checkIntandPass(commandList[2], output)
                    day.setTotal(output)
            if (not dateFound):
                print("Error: invalid day")
                
        elif (keyword == "print"): #print
            if (commandList[1] == "all"):
                for day in daysOfTheWeek:
                    print(day)
            else:
                printDay = False
                for day in daysOfTheWeek:
                    if (day.name() == commandList[1]):
                        print(day)
                        printDay = True
                        break
                if (not printDay):
                    print("Error: invalid day")

        elif (keyword == "list"):
            if (commandList[1] == "all"):
                for course in courses:
                    print(course)
            else:
                printed = False
                for course in courses:
                    if (commandList[1] == courses):
                        print(course)
                        printed = True
                if (not printed):
                    print("Error: course not found")

        elif (keyword == "exit"):
            print("Goodbye")
            exit = True
        
        #recalculate function needed
    

if __name__ == "__main__":
    main()
