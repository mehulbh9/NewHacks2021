from assignment import Assignment
from course import Course
from day import Day
from exam import Exam
import datetime
def readFile(fileName):
    file = open(fileName, "r", encoding = "UTF-8")
    line = file.readline()
    line = line[0: len(line)]

    list1 = line.split("*")

    returnList = []
    for l1 in list1:
        list2 = l1.split("&")
        temp = Course(list2[0], int(list2[1]), int(list2[2]))

        if(list2[3] != "$"):
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

        if(list2[4] != "$"):
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
                x = str(date)

                tempExam = Exam(name, weight, studytime, date)
                temp.exams.append(tempExam)

        returnList.append(temp)
    file.close()
    return returnList

def writeFile(courses, fileName):
    string = ""
    for course in courses:
        string += course.name + ""
        string += "&"
        string += str(course.priority) + ""
        string += "&"
        string += str(course.difficulty) + ""
        string += "&"

        if(len(course.assignments) == 0):
            string += "$ "
        else:
            for asn in course.assignments:
                string += asn.name
                string += "^"

                date_and_time = str(asn.duedate)
                temp_date = date_and_time.split()
                date = temp_date[0].split("-")

                string += date[0]
                string += "^"
                string += str(int(date[1]))
                string += "^"
                string += str(int(date[2]))
                string += "^"

                string += str(asn.time)
                string += ","

        string = string[0: len(string) - 1]
        string += "&"

        if(len(course.exams) == 0):
            string += "$ "
        else:
            for exam in course.exams:
                string += exam.name
                string += "^"
                string += str(exam.weight)
                string += "^"
                string += str(exam.study_time)
                string += "^"

                date_and_time = str(exam.date)
                temp_date = date_and_time.split()
                date = temp_date[0].split("-")

                string += date[0]
                string += "^"
                string += str(int(date[1]))
                string += "^"
                string += str(int(date[2]))

                string += ","
        string = string[0: len(string) - 1]
        string += "*"
    string = string[0: len(string) - 1]
    file = open(fileName, "w", encoding = "UTF-8")
    file.write(string)
    file.close()



#Math1234&1&1&Math1234%HW1^2020^5^6^500,Math1234%HW2^2020^5^15^500&Math1234%Midterm^10.0^6^2020^8^9*Eng45&1&1&$&$
myList = readFile("testFile.txt")
writeFile(myList, "testFile2.txt")
