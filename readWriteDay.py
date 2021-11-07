def readDays(fileName):
    day_and_totalTime = {}
    file = open(fileName, "r", encoding = "UTF-8")
    line = file.readline()

    daysInfo = line.split("*")

    for i in range (7):
        temp = daysInfo[i].split("^")
        curDay = temp[0]
        time = int(temp[1])
        day_and_totalTime[curDay] = time
    file.close()
    return day_and_totalTime

def readDays (fileName, days):
    string = ""
    for i in range(7):
        string += days[i].name
        string += "^"
        string += str(days[i].timeTotal)
        string += "*"
    string = string[0:len(string) - 1]

    file = open(fileName, "w", encoding = "UTF-8")
    file.write(string)
    file.close()

#x = readDays("testFile3.txt")
#print(x)
