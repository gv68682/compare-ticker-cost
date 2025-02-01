import os
import json
from icecream import ic
from dotenv import load_dotenv
from datetime import datetime

import service.requests as req
import util.crud as crud
import util.csv as csv
import util.compare as compare



def executionTime(start, end):
    executionTime="m"
    totalTime = end - start
    minutes = round(totalTime.total_seconds()/60, 2)
    seconds = round(totalTime.total_seconds(), 2)
    milliSeconds = round(totalTime.total_seconds()*1000, 2)

    if milliSeconds < 1000:
        executionTime = f"{milliSeconds}", "MS"
    elif seconds <60:
        executionTime = f"{seconds}", "S"
    else:
        executionTime = f"{minutes}", "M"

    return executionTime 



def formatTime(path, time):
    formattedTime = time.replace(microsecond=0)
    timeToStr = str(formattedTime)
    childFoler = os.path.join(path, timeToStr)
    return childFoler



def createCsvExcelFolders(path, name):
    childFolder = os.path.join(path, name)
    currentPath = "current"f"{name}""Path"
    appContext[currentPath]=str(childFolder)
    os.makedirs(childFolder, exist_ok=True)



def createFolder(path, time):
    folderPath = os.path.abspath(path)
    if os.path.isdir(folderPath):
        childFolder = formatTime(path, time)
        os.makedirs(childFolder, exist_ok=True)
        createCsvExcelFolders(childFolder, "csv")
        createCsvExcelFolders(childFolder, "excel")
    else:
        os.makedirs(path, exist_ok=True)
        childFolder = formatTime(path, time)
        os.makedirs(childFolder, exist_ok=True)
        createCsvExcelFolders(childFolder, "csv")
        createCsvExcelFolders(childFolder, "excel")



def getEnv():
    load_dotenv('.env')
    envDict={
        "apiKey": os.getenv("APIKEY"),
        "baseUrl": os.getenv("BASEURL"),
        "importsFileName": os.getenv("IMPORTFILENAME"),
        "exportsFileName": os.getenv("EXPORTFILENAME")
    }
    return envDict

appContext = {}
configJson = "./config.json"
with open(configJson) as c:
    configDict = json.load(c)

appContext['env']=getEnv()
appContext["importsFilePath"]=configDict["paths"]["importsFilePath"]
appContext["exportsFilePath"]=configDict["paths"]["exportsFilePath"]
appContext["csvHeaders"]=configDict["paths"]["csvHeaders"]
appContext["csvHeadersToCompare"]=configDict["paths"]["csvHeadersToCompare"]



def execution():
    startTime = datetime.now()

    # finnhub_client = req.makeConnection(appContext['env']["apiKey"])
    result = crud.makeRequestBit(appContext["env"]["baseUrl"])
    createFolder(appContext["exportsFilePath"], startTime)
    csv.writeCsv(appContext, result)
    compare.compare(appContext)

    endTime = datetime.now()
    totalExecutionTime =executionTime(startTime, endTime)
    ic(totalExecutionTime)


if __name__ == "__main__":
    execution()