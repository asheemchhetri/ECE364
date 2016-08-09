import re
def getAddress(sentence):
    m=re.search(r"[a-fA-F0-9]{2}[\:|\-][a-fA-F0-9]{2}[\:|\-][a-fA-F0-9]{2}[\:|\-][a-fA-F0-9]{2}[\:|\-][a-fA-F0-9]{2}[\:|\-][a-fA-F0-9]{2}",sentence)
    if m:
        return m.group(0)
    else:
        return None

def getSwitches(commandline):
    m=re.findall(r"[\+|\\]([a-z])\s+([^\\\+\s]+)",commandline)
    m.sort()
    return m

def getElements(fullAddress):
    m=re.match(r"https?\:\/\/([a-zA-Z0-9\.]+)\/([a-zA-Z0-9]+)\/([a-zA-Z0-9]+)",fullAddress)
    if m and fullAddress == m.group(0):
        return (m.group(1),m.group(2),m.group(3))
    else:
        return None