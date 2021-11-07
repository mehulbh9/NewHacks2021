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
    return day_and_totalTime

#x = readDays("testFile3.txt")
#print(x)

