import json
from icecream import ic
import datetime



def unixToRealTime(timeStamp):
    datetimeObj = datetime.datetime.fromtimestamp(int(timeStamp))
    return str(datetimeObj)


def orderValues(obj):
    row = [0] * 13 
    for key in obj:
        if   key == "pair": row[0]=obj[key]
        elif key == "last": row[1]=obj[key]
        elif key == "timestamp": convertedTime= unixToRealTime(obj[key]);row[2]=convertedTime
        elif key == "open": row[3]=obj[key]
        elif key == "high": row[4]=obj[key]
        elif key == "low": row[5]=obj[key]
        elif key == "percent_change_24": row[6]=obj[key]
        elif key == "bid": row[7]=obj[key]
        elif key == "ask": row[8]=obj[key]
        elif key == "side": row[9]=obj[key]
        elif key == "open_24": row[10]=obj[key]
        elif key == "volume": row[11]=obj[key]
        else: row[12]=obj[key]
    return row



def orderFewValues(obj):
    row = [0] * 3 
    for key in obj:
        if   key == "pair": row[0]=obj[key]
        elif key == "last": row[1]=obj[key]
        elif key == "timestamp": convertedTime= unixToRealTime(obj[key]);row[2]=convertedTime
    return row
     


def dataToList(resultList, appContext):
    toPythonDict = json.loads(resultList)
    valList=[]
    fewValList=[]
    for obj in toPythonDict:
        row = orderValues(obj)
        valList.append(row)
        r = orderFewValues(obj)
        fewValList.append(r)
    appContext["newDataToCompare"]= fewValList 
    return valList
   



