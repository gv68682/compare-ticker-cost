import csv
from icecream import ic

import util.read as read
import util.compare as compare



def writeCsv(appContext, resultList):
    folderPath = appContext["currentcsvPath"]
    csvHeaders = appContext["csvHeaders"]
    capitalizedCsvHeaders = [word.upper() for word in csvHeaders]
    valList = read.dataToList(resultList, appContext)
   
    with open(folderPath+"/data.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(capitalizedCsvHeaders)
        for row in valList:
         writer.writerow(row)




def readCsv(path, file):
   with open(f"{path}/{file}", newline='' ) as readcsv:
      read = csv.reader(readcsv)
      valList = list(read)
      return valList
   


def writeCsvToCompare(appContext, oldDataList):
    folderPath = appContext["currentcsvPath"]
    csvHeadersToCompare = appContext["csvHeadersToCompare"]
    capitalizedCsvHeaders = [word.upper() for word in csvHeadersToCompare]
    newDataToCompare = appContext["newDataToCompare"]
    listToCompare = compare.orderValToCompare(oldDataList, newDataToCompare)
    
    with open(folderPath+"/compared.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(capitalizedCsvHeaders)
        for row in listToCompare:
         writer.writerow(row)
   