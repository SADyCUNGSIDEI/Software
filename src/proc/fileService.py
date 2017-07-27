import json


def saveRegistroData(filename, data):

    if not filename.endsWith(".sre"):
        filename += ".sre"

    fileToWrite = open(filename, "w")

    fileToWrite.write(json.dumps(data))


def openGraficoData(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()

    return json.loads(data)
