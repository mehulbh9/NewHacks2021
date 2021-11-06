def calculateTime(courses, days):
    totalTimeFree = 0
    totalTimeWork = 0
    assignmentList = []
    assignmentDueDateList = []

    for course in courses:
        for assignment in course.assignments():
            totalTimeWork += assignment.time()
            assignmentList.append(assignment.name())
            assignmentDueDateList.append(assignment.getDay())
    
    for day in days:
        totalTimeFree += day.totalTime()
    
    #finding earliest due date
    while (len(assignmentList) > 0):
        lowest = 1000
        lowestIndex = -1
        for i in range(len(assignmentList)):
            if (assignmentDueDateList[i] < lowest):
                lowest = assignmentDueDateList[i]
                lowestIndex = i
        