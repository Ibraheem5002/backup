import datetime

def getTime():
    data = datetime.datetime.now()

    # data.hour
    # data.minute
    # data.second

    return data.time()

def getDate():
    data = datetime.datetime.now()

    # data.year
    # data.month
    # data.second

    return data.date()