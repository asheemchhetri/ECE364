def checkTypes(l):
    if type(l) != list or not l:
        return None
    else:
        intc=0
        strc=0
        fltc=0
        for item in l:
            if type(item) == int:
                intc+=1
            elif type(item) == str:
                strc+=1
            else:
                fltc+=1

    return [intc,fltc,strc]

def normalizeVector(l):
    if type(l) != list or not l:
        return None
    else:
        mag=0
        for item in l:
            mag+=item**2
        mag=mag**0.5
        for item1 in l:
            item1 /= mag
            print(item1)
    return l

def findMedian(l):
    if type(l) != list or not l:
        return None
    else:
        for item in l:
            if type(item) != int or type(item) != float:
                return None

def rectifySignal(l):
    if type(l) != list or not l:
        return None
    else:
        i=0
        while i < len(l):
            if l[i] < 0:
                l[i] =0
            i+=1

    return l

def convertToBoolean(l):
    if type(l) != int or l > 2**8:
        return None
    string = bin(l)
    string = string [2:]
    list = [0]*len(string)
    i=0
    while i< len(list):
        if string[i] == '0':
            list[i]=False
        else:
            list[i]=True
        i+=1
    return list

def convertToInteger(l):
    if not l or type(l) != list:
        return None
    val=0
    l.reverse()
    i=0
    while i<len(l):
        if type(l[i]) != bool:
            return None
        else:
            val+=l[i]*2**i
        i+=1
    return val



if __name__ == '__main__':
    normalizeVector([0,1,2,3,4,10])
