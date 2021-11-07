import datetime
from assignment import Assignment
from course import Course
from day import Day
from exam import Exam

def makeDay(name):
    day = Day(name)
    return day

def checkNumInputs(list, length):
    if (len(list) < length):
        print("Error: too few arguments")
        return False
    elif (len(list) > length):
        print("Error: too many arguments")
        return False
    else:
        return True

    
def printHelp():
    print("type 'help [command]' to see arguments of [command]")
    print("List of Commands: \nhelp \ncourse \nassignment \ntime \nprint \nlist")

def main():
    namesOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #array of names of the week in string
    keywordList = ["help", "course", "assignment", "time", "print", "list"]
    daysOfTheWeek = [] #array of Day objects
    courses = [] #array of Course objects
    exit = False #whether or not while loop continues

    for name in namesOfTheWeek:
        daysOfTheWeek.append(makeDay(name))

    while(not exit):
        try : 
            command = str(input(">> "))
        except ValueError:
            print("Enter a valid command.")
            continue

        commandList = command.split()
        keyword = commandList[0]
        
        if (keyword == "help"):
            
            if (len(commandList) == 1):
                printHelp()
            else:
                helpcom = commandList[1]
                if (helpcom == "help"):
                    print("Description: used to show format of other commands")
                    print("help [command]")
                elif (helpcom == "course"):
                    print("Description: used to add or delete a course")
                    print("course [add/delete]")
                elif (helpcom == "assignment"):
                    print("Description: used to add or delete an assignment from a course")
                    print("assignment [add/delete]")
                elif (helpcom == "time"):
                    print("Description: used to set the total time available of a certain day of week")
                    print("time [day of the week] [total time available]")
                elif (helpcom == "print"):
                    print("Description: prints the schedule of a day, or every day")
                    print("print ['day'/all]")
                elif (helpcom == "list"):
                    print("Description: prints all the courses, assignments, and exams")
                    print("list ['course'/all]")
                elif (helpcom == "exam"):
                    print("Description: used to add or delete an exam from a course")
                    print("exam [add/delete]")
                
        elif (keyword == "course"): #course
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

                print("Does the following course have low, neutral, or high priority")
                while True:
                    try:
                        str_priority = str(input("Enter the priority (low, neutral, or high) : ")).lower()
                    except ValueError:
                        print("Please enter low, neutral, or high.")
                        continue
                    if (str_priority == "low"):
                        priority = 1
                        break
                    elif (str_priority == "neutral"):
                        priority = 2
                        break
                    elif (str_priority == "high"):
                        priority = 3
                        break
                    else: 
                        print("Please enter low, neutral, or high.")
                    
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
                
                print("Are you sure you want to delete the course", name, "?")
                while True:
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
                        break     
                    elif (delete_course == "no"):
                        break
                    else:
                        print("Please enter yes or no")
            else:
                print("Please enter a valid command. Use the command \'help\'.")

                    
        elif (keyword == "assignment"): #assignment
            if (len(courses) == 0):
                print("You do not have any courses. Please make a course first.") 
                continue
            if (commandList[1] == "add"):
                print("You currently have the following courses: ")
                for i in range(0, len(courses)): 
                    print ((i + 1), ".", (courses[i].name))
                while True:
                    try: 
                        course_index = int(input("Indicate the number of the course that this assignment belongs to : ")) - 1
                    except ValueError:
                        print("Please enter a valid number between 1 and", len(courses))
                        continue
                    if (course_index < 0 or course_index >= len(courses)):
                        print("Please enter a valid number between 1 and", len(courses))
                    else: 
                        break
                
                while True:
                    try:
                        name = str(input("What is the name of the assignment? : "))
                    except ValueError:
                        print("Invalid input. Please enter a string.")
                        continue
                    already_exists = False
                    for assignment in courses[course_index].assignments:
                        if (assignment.name == name):
                            already_exists = True
                            break
                    if (already_exists):
                        print("An assignment with this name already exists, please enter a new assignment.")
                    else:
                        break

                while True:
                    try: 
                        time = int(input("In minutes, how long do you think the assignment will take to complete? : "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                    if (time < 0 or time > 1440):
                        print("Please enter a valid amount of time under that of a day.")
                    else:
                        break

                print("When is the assignment due?")
                while True: 
                    try: 
                        daymonthyear = str(input("Enter the date (day,month,year) : ")).split(",")
                    except ValueError:
                        print("Enter a valid date with the correct format.")
                        break

                    if (int(daymonthyear[1]) < 1 or int(daymonthyear[1]) > 12):
                        print("Please enter a number between 1 and 12.")
                        continue
                    if (int(daymonthyear[2]) < 2021 or int(daymonthyear[2]) > 2022):
                        print("Please enter whether the exam is in 2021 or 2022.")
                        continue
                    if (int(daymonthyear[1]) == 2):
                        if (int(daymonthyear[0]) < 1 or int(daymonthyear[0]) > 28):
                            print("Please enter a date between 1 and 28")
                            continue
                    elif (int(daymonthyear[1]) == 4 or int(daymonthyear[1]) == 6 or int(daymonthyear[1]) == 9 or int(daymonthyear[1]) == 11):
                        if (int(daymonthyear[0]) < 1 or int(daymonthyear[0]) > 30):
                            print("Please enter a date between 1 and 30")
                            continue
                    else:
                        if (int(daymonthyear[0]) < 1 or int(daymonthyear[0]) > 31):
                            print("Please enter a date between 1 and 31")
                            continue
                    break

                courses[course_index].assignments.append(Assignment(courses[course_index].name + "%" + name, datetime.datetime(int(daymonthyear[2]), int(daymonthyear[1]), int(daymonthyear[0])), time))
                
            elif (commandList[1] == "delete"):
                print("You currently have the following courses: ")
                for i in range(0, len(courses)): 
                    print ((i + 1), ".", (courses[i].name))
                while True:
                    try: 
                        course_index = int(input("Indicate the number of the coure you would like to delete an assignment from : ")) - 1
                    except ValueError:
                        print("Please enter a valid number between 1 and", len(courses))
                        continue
                    if (course_index < 0 or course_index >= len(courses)):
                        print("Please enter a valid number between 1 and", len(courses))
                    else: 
                        break
                
                if (len(courses[course_index]) == 0):
                    print("There are no assignments in this course.")
                    break

                while True:
                    try:
                        name = str(input("What is the name of the assignment? : "))
                    except ValueError:
                        print("Invalid input. Please enter a string.")
                        continue
                    already_exists = False
                    for assignment in courses[course_index].assignments:
                        if (assignment.name == name):
                            already_exists = True
                            break
                    if (not(already_exists)):
                        print("This assignment does not exist. Please enter a valid assignment.")
                    else:
                        break

                print("Are you sure you want to delete the assignment", name, "?")
                while True:
                    try: 
                        delete_assignment = str(input("Enter yes or no : ")).lower()
                    except ValueError: 
                        print("Please enter yes or no")
                        continue
                    if (delete_assignment == "yes"):
                        for assignment in courses[course_index].assignments: 
                            if (assignment.name == name):
                                courses[course_index].assignments.remove(assignment)
                                break
                    elif (delete_assignment == "no"):
                        break
                    else:
                        print("Please enter yes or no")
            else :
                print("Please enter a valid command. Use the command \'help\'")

        elif (keyword == "exam"):
            if (len(courses) == 0):
                print("You do not have any courses. Please make a course first.") 
                continue
            if (commandList[1] == "add"):
                print("You currently have the following courses: ")
                for i in range(0, len(courses)): 
                    print ((i + 1), ".", (courses[i].name))
                while True:
                    try: 
                        course_index = int(input("Indicate the number of the course that this exam belongs to : ")) - 1
                    except ValueError:
                        print("Please enter a valid number between 1 and", len(courses))
                        continue
                    if (course_index < 0 or course_index >= len(courses)):
                        print("Please enter a valid number between 1 and", len(courses))
                    else: 
                        break
                
                while True:
                    try:
                        name = str(input("What is the name of the exam? : "))
                    except ValueError:
                        print("Invalid input. Please enter a string.")
                        continue
                    already_exists = False
                    for exam in courses[course_index].exams:
                        if (exam.name == name):
                            already_exists = True
                            break
                    if (already_exists):
                        print("An exam with this name already exists, please enter a new exam.")
                    else:
                        break

                while True:
                    try:
                        weight = float(input("What is the weight of this exam? : "))
                    except ValueError:
                        print("Please enter a valid number greater than 0 and less than 100")
                        continue
                    if (weight <= 0 or weight >= 100):
                        print("Please enter a valid number greater than 0 and less than 100")
                    else:
                        break

                while True:
                    try: 
                        time = int(input("In minutes, how long do you think you should study for the exam? : "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                    if (time < 0 or time > 1440):
                        print("Please enter a valid amount of time under that of a day.")
                    else:
                        break

                print("When is the exam?")
                while True: 
                    try: 
                        daymonthyear = str(input("Enter the date (day,month,year) : ")).split(",")
                    except ValueError:
                        print("Enter a valid date with the correct format.")
                        break

                    if (int(daymonthyear[1]) < 1 or int(daymonthyear[1]) > 12):
                        print("Please enter a number between 1 and 12.")
                        continue
                    if (int(daymonthyear[2]) < 2021 or int(daymonthyear[2]) > 2022):
                        print("Please enter whether the exam is in 2021 or 2022.")
                        continue
                    if (int(daymonthyear[1]) == 2):
                        if (int(daymonthyear[0]) < 1 or int(daymonthyear[0]) > 28):
                            print("Please enter a date between 1 and 28")
                            continue
                    elif (int(daymonthyear[1]) == 4 or int(daymonthyear[1]) == 6 or int(daymonthyear[1]) == 9 or int(daymonthyear[1]) == 11):
                        if (int(daymonthyear[0]) < 1 or int(daymonthyear[0]) > 30):
                            print("Please enter a date between 1 and 30")
                            continue
                    else:
                        if (int(daymonthyear[0]) < 1 or int(daymonthyear[0]) > 31):
                            print("Please enter a date between 1 and 31")
                            continue
                    break

                courses[course_index].exams.append(Exam(courses[course_index].name + "%" + name, weight, time, datetime.datetime(daymonthyear[2], daymonthyear[1], daymonthyear[0])))
                
            elif (commandList[1] == "delete"):
                print("You currently have the following courses: ")
                for i in range(0, len(courses)): 
                    print ((i + 1), ".", (courses[i].name))
                while True:
                    try: 
                        course_index = int(input("Indicate the number of the coure you would like to delete an exam from : ")) - 1
                    except ValueError:
                        print("Please enter a valid number between 1 and", len(courses))
                        continue
                    if (course_index < 0 or course_index >= len(courses)):
                        print("Please enter a valid number between 1 and", len(courses))
                    else: 
                        break
                
                if (len(courses[course_index]) == 0):
                    print("There are no exams in this course.")
                    break

                while True:
                    try:
                        name = str(input("What is the name of the exam? : "))
                    except ValueError:
                        print("Invalid input. Please enter a string.")
                        continue
                    already_exists = False
                    for exam in courses[course_index].exams:
                        if (exam.name == name):
                            already_exists = True
                            break
                    if (not(already_exists)):
                        print("This exam does not exist. Please enter a valid exam.")
                    else:
                        break

                print("Are you sure you want to delete the exam", name, "?")
                while True:
                    try: 
                        delete_exam = str(input("Enter yes or no : ")).lower()
                    except ValueError: 
                        print("Please enter yes or no")
                        continue
                    if (delete_exam == "yes"):
                        for exam in courses[course_index].exams: 
                            if (exam.name == name):
                                courses[course_index].exams.remove(exam)
                                break
                    elif (delete_exam == "no"):
                        break
                    else:
                        print("Please enter yes or no")
            else :
                print("Please enter a valid command. Use the command \'help\'")

        elif(keyword == "time"): #time
            timeTotal = 0
            dateFound = False
            for day in daysOfTheWeek:
                if (commandList[1] == day.name()):
                    dateFound = True
                    try: 
                        timeTotal = int(commandList[2])
                        day.setTotal(timeTotal)
                        dateFound = True
                    except ValueError:
                        print("invalid input")
            if (not dateFound):
                print("Error: invalid day")
                
        elif (keyword == "print"): #print
            ####
            totalTimeFree = 0.0
            totalTimeWork = 0.0
            assignmentTime = []
            assignmentList = []
            assignmentDueDateList = []
            assignmentDifficulty = []
            assignmentPriority = []
            targetTimeRatio = 0.0
            todaysDatetime = datetime.datetime.now()
            todaysDate = int(todaysDatetime.strftime("%j"))
            todaysDateName = todaysDatetime.strftime("%A")
            dayIndex = 0

            if (todaysDate <= 120):
                todaysDate+=366

            for course in courses:
                for assignment in course.assignments:
                    totalTimeWork += assignment.time
                    assignmentTime.append(assignment.time)
                    assignmentList.append(assignment)
                    assignmentDueDateList.append(assignment.getDay())
                    assignmentDifficulty.append(course.difficulty)
                    assignmentPriority.append(course.priority)
                
            for day in daysOfTheWeek:
                totalTimeFree += day.timeTotal

            targetTimeRatio = totalTimeWork/totalTimeFree

            for day in daysOfTheWeek:
                if (todaysDateName != day.name):
                    dayIndex+=1

                day.targetTime = float(targetTimeRatio * day.timeTotal)

                
            #finding earliest due date
            while (len(assignmentList) > 0):
                lowest = 1000   
                lowestIndex = -1
                tempDate = todaysDate
                timeDifference = 10000.0
                for i in range(len(assignmentList)):
                    if (assignmentDueDateList[i] < lowest):
                        lowest = assignmentDueDateList[i]
                        lowestIndex = i
                    elif (assignmentDueDateList[i] == lowest):
                        if (assignmentPriority[i] > assignmentPriority[lowestIndex]):
                            lowestIndex = i

                while (tempDate != assignmentDueDateList[lowestIndex]):
                    if (timeDifference > abs(assignmentTime[lowestIndex] - daysOfTheWeek[tempDate].targetTime)):
                        timeDifference = abs(assignmentTime[lowestIndex] - daysOfTheWeek[tempDate].targetTime)
                        
                    tempDate+=1

                    if (dayIndex < 6):
                        dayIndex+=1
                    elif (dayIndex == 6):
                        dayIndex = 0

                daysOfTheWeek[dayIndex].assignments.append(assignmentList[lowestIndex])
                daysOfTheWeek[dayIndex].timeWork += assignmentTime[lowestIndex]
                daysOfTheWeek[dayIndex].targetTime -= assignmentTime[lowestIndex]
                assignmentTime.pop(lowestIndex)
                assignmentList.pop(lowestIndex)
                assignmentDueDateList.pop(lowestIndex)
                assignmentDifficulty.pop(lowestIndex)
                assignmentPriority.pop(lowestIndex)

            ####
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
                if (len(courses) == 0):
                    print("There are no courses")
                else:
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

        

if __name__ == "__main__":
    main()
