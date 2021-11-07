from assignment import Assignment
from course import Course
from day import Day
from exam import Exam
import datetime
def readFile(fileName):
    file = open(fileName, "r", encoding = "UTF-8")
    line = file.readline()

    list1 = line.split("*")

    returnList = []
    for l1 in list1:
        list2 = l1.split("&")
        temp = Course(list2[0], list2[1], list2[2])

        list3 = list2[3].split(",")
        for assignment in list3:
            asnAttributes = assignment.split("^")

            name = asnAttributes[0]
            year = int(asnAttributes[1])
            month = int(asnAttributes[2])
            day = int(asnAttributes[3])
            time = int(asnAttributes[4])

            date = datetime.datetime(year, month, day)

            tempAssignment = Assignment(name, date, time)
            temp.assignments.append(tempAssignment)

        list4 = list2[4].split(",")
        for exams in list4:
            examAttributes = exams.split("^")

            name = examAttributes[0]
            weight = float(examAttributes[1])
            studytime = int(examAttributes[2])
            year = int(examAttributes[3])
            month = int(examAttributes[4])
            day = int(examAttributes[5])

            date = datetime.datetime(year, month, day)

            tempExam = Exam(name, weight, studytime, date)
            temp.exams.append(tempExam)

        returnList.append(temp)
    return returnList

#Math1234&1&1&HW1^2020^5^6^500,HW2^2020^5^15^500&Math^10^6^7^8^9
myList = readFile("testFile.txt")
print(myList[0])
