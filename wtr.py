from assignment import Assignment
from course import Course
from day import Day
from exam import Exam
import datetime

def writeFile(Course):
    # "*" is used to separate different courses
    # "&" is used to separate course attributes (i.e. name, priority, difficiulty...)
    # "," is used to separate different assignments and exams
    # "^" is used to separate assignment and exam attributes (i.e. weight, year, month, day, time...)
    str=""
    for course in Course:
        str.append(course.name)
        str.append("&")
        str.append(course.priority)
        str.append("&")
        str.append(course.difficult)
        str.append("&")
        for asn in course.assignments:
            for attr in asn:
                str.append(attr)
                str.append("^")
            str.pop()
            str.append(",")
        for exam in course.exams:
            for attr in exam:
                str.append(attr)
                str.append("^")
            str.pop()
            str.append(",")        
        str.pop()
        str.append("*") #in the end
    str.pop()
    with open("plswork.txt","a") as f:
        f.write(str)
        
        
        
