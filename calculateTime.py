def calculateTime(courses, days):
    totalTimeFree = 0.0
    totalTimeWork = 0.0
    assignmentList = []
    assignmentDueDateList = []
    assignmentDifficulty = []
    assignmentPriority = []
    targetTimeRatio = 0.0

    for course in courses:
        for assignment in course.assignments():
            totalTimeWork += assignment.time()
            assignmentList.append(assignment.name())
            assignmentDueDateList.append(assignment.getDay())
            assignmentDifficulty.append(course.difficulty())
            assignmentPriority.append(course.priority())
    
    for day in days:
        totalTimeFree += day.timetotal()

    targetTimeRatio = totalTimeWork/totalTimeFree

    for day in days:
        day.targetWork() = float(targetTimeRatio * day.timetotal())

    
    #finding earliest due date
    while (len(assignmentList) > 0):
        lowest = 1000   
        lowestIndex = -1
        for i in range(len(assignmentList)):
            if (assignmentDueDateList[i] < lowest):
                lowest = assignmentDueDateList[i]
                lowestIndex = i
            elif (assignmentDueDateList[i] == lowest):
                if (assignmentPriority[i] > assignmentPriority[lowestIndex]):
                    lowestIndex = i
        
