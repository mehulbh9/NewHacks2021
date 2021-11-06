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
        try : 
            command = str(input("Enter a command : "))
        except ValueError:
            print("Enter a valid command.")
            continue

        commandList = command.split()
        keyword = commandList[0]

        input(">> ")
        
        if (keyword == "course"): #course
            if (commandList[1] == "add"):
                while True:
                    try:
                        name = str(input("What is the name of the course? : "))
                    except ValueError:
                        print("Invalid input. Please enter a string.")
                        continue
                    already_exists = False
                    for course in courses:
                        if (course.name == name):
                            already_exists = True
                            break
                    if (already_exists):
                        print("A course with this name already exists, please enter a new course.")
                    else:
                        break
                if (len(courses) == 0):
                    priority = 0; 
                else :
                    print("You currently have the following courses: ")
                    for i in range(0, len(courses)): 
                        print ((i + 1), ".", (courses[i].name))
                    print("Does the following course have lower, the same, or higher priority compared to your other courses?")
                    while True:
                        try:
                            str_priority = str(input("Enter the priority (low, same, or high) : ")).lower()
                        except ValueError:
                            print("Please enter low, same, or high.")
                            continue
                        if (str_priority == "low"):
                            priority = 1
                            break
                        elif (str_priority == "same"):
                            priority = 2
                            break
                        elif (str_priority == "high"):
                            priority = 3
                            break
                        else: 
                            print("Please enter low, same, or high.")
                    
                while True:
                    try: 
                        difficulty = int(input("What would you say the difficulty of the course is out of 5? : "))
                    except ValueError:
                        print("Please enter a number between 1 and 5.")
                    
                    if (difficulty < 0 or difficulty > 5):
                        print("Please enter a number between 1 and 5.")
                    else:
                        break
                courses.append(Course(name, priority, difficulty))

            elif (commandList[1] == "delete"):
                while True:
                    try:
                        name = str(input("What is the name of the course? : "))
                    except ValueError:
                        print("Invalid input. Please enter a string.")
                        continue
                    already_exists = False
                    for course in courses:
                        if (course.name == name):
                            already_exists = True
                            break
                    if (not(already_exists)):
                        print("This course does not exist. Please enter a valid course.")
                    else:
                        break
                print("Are you sure you want to delete this course?")
                try: 
                    delete_course = str(input("Enter yes or no : ")).lower()
                except ValueError: 
                    print("Please enter yes or no")
                    continue
                if (delete_course == "yes"):
                    for course in courses: 
                        if (course.name == name):
                            courses.remove(course)
                            break
                elif (delete_course == "no"):
                    break
                else:
                    print("Please enter yes or no")
            else:
                print("Please enter a valid command. Use the command \'help\'.")

                
                
        elif (keyword == "assignment"): #assignment
            if (commandList[1] == "add"):
                pass
            elif (commandList[1] == "delete"):
                pass
            else :
                print("Please enter a valid command. Use the command \'help\'")

        elif (keyword == "exam"):
            if (commandList[1] == "add"):
                pass
            elif (commandList[1] == "delete"):
                pass
            else :
                print("Please enter a valid command. Use the command \'help\'")

        elif(keyword == "time"): #time

            output = 0
            dateFound = False
            for day in daysOfTheWeek:
                if (commandList[1] == day.name()):
                    dateFound = True
                    if (checkIntandPass(commandList[2], output)):
                        day.setTotal(output)
                    else:
                        print("invalid input")
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
