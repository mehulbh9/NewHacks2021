from assignment import Assignment
from course import Course
from day import Day
from exam import Exam
def readFile(fileName):
    file = open(fileName, "r", encoding = "UTF-8")
    line = file.readline()

    list1 = line.split("*")

    for l1 in list1:
        list2 = l1.split("&")
        temp = Course(list2[0], list2[1], list2[2])

        list3 = list2[3].split(",")
        for assignment in list3:
            asnAttributes = assignment.split("^")
            name = asnAttributes[0]
            course = asnAttributes[1]
            difficulty = int(asnAttributes[2])
            date = int(asnAttributes[3])

            tempAssignment = Assignment(name, course)
            tempAssignment.difficulty = difficulty
            tempAssignment.date = date

            temp.assignments.append(tempAssignment)

        list4 = list2[4].split(",")
        for exams in list4:
            examAttributes = exams.split("^")
            weight = int(examAttributes[0])
            importance = int(examAttributes[1])
            studytime = int(examAttributes[2])
            course = examAttributes[3]
            day = int(examAttributes[4])

            tempExam = Exam(weight, importance, studytime, course, day)

            temp.exams.append(tempExam)




#Sample Input: Math1234&1&1&HW1^Math1234^4^9,HW2^Eng1234^3^5&30^3^10^Math1234^8
readFile("testFile.txt")
