import json

from .Person import data



def printResults():
    """
    """
    global data
    print(json.dumps(data, indent=4))


def getResutls():
    """
    """
    global data
    return data