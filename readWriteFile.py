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

        print("Name =", list2[0])
        print("Priority =", list2[1])
        print("Difficulty =", list2[2])
        print("Assignments =", list2[3])
        print("Exams =", list2[4])

        list3 = list2[3].split(",")
        print(list3)

readFile("testFile.txt")
