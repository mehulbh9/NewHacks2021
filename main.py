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
    courses = []
    exit = False

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
            pass
        elif(keyword == "time"): #time
            pass
        elif (keyword == "print"): #print
            pass
        elif (keyword == "exit"):
            exit = True
    

if __name__ == "__main__":
    main()
