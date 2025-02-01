import os
import util.csv as csv



def compare(appContext):
    importsPath = appContext["importsFilePath"]
    filePath = os.path.abspath(importsPath)
    oldDataFileName = appContext["env"]["importsFileName"]
    oldData = csv.readCsv(filePath, oldDataFileName)
    csv.writeCsvToCompare(appContext, oldData)



def splitDate(dateStr):
    if dateStr:
        arr = dateStr.split()
        return arr[0]



def currentLowOrHigh(ol, nl):
    result = "High" if nl > ol else "Low"
    return result
    


def orderValToCompare(oldList, newList):
    combinedList=[]
    l = max(len(oldList), len(newList))
    finallen = len(newList) if l == len(oldList) else len(oldList)
  
    for i in range(finallen-1):
        ticker = oldList[i][0]
        row = []
        for arr in newList:
            if arr[0] == ticker:
                olGetYearOnly = splitDate(oldList[i][2])
                nlGetYearOnly = splitDate(arr[2])
                comparedResult = currentLowOrHigh(oldList[i][1], arr[1])
                row.append(oldList[i][0])
                row.append(oldList[i][1])
                row.append (arr[1])
                row.append(olGetYearOnly)
                row.append (nlGetYearOnly)
                row.append(comparedResult)
                combinedList.append(row)
                break
    return combinedList
