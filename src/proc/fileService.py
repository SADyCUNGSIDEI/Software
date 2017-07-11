import json

def saveRegistroData(filename, data):

    if not filename.endsWith(".sre"):
        filename += ".sre"

    fileToWrite = open(filename, "w")

    fileToWrite.write(json.dumps(data))


