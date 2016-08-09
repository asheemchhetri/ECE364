def getAverage(l):
    val = sum(l[:])
    count = len(l)
    return val/count

def getHeadAverage(l, n):
    val = sum(l[:n])

    return val/n

def getTailMax(l, m):
    l.reverse()
    l = l[:m]
    l.sort()
    return l[-1]

def getNumberAverage(l):
    val=0
    cnt=0
    for item in l:
        if type(item) == int or type(item) == float:
            val+=item
            cnt+=1
    return val/cnt

def getFormattedSSN(n):
    string = str(n)
    while len(string) < 9:
        string = "0"+ string
    print("{}-{}-{}".format(string[:3],string[3:5],string[5:9]))

def findName(l,s):
    for item in l:
        item = str(item).split()
        if s in item:
            return " ".join(item)
    return 0

def getColumnSUm(mat):
    i=0
    val = [0]*len(mat[0])

    for item in mat:

        for item1 in item:

            val[item.index(item1)] += item1

    return val

def getFormattedNames(ln):
    print('"{}, {} {}."'.format(ln[2],ln[0],ln[1]))

def getElementwiseSum(l1,l2):
    if len(l1) > len(l2):
        size = len(l2)
        l3 = l1
    else:
        size = len(l1)
        l3 = l2
    i=0

    while size > i:
        l3[i] += l2[i]
        i+=1
    return l3

def removeDuplicates(l):
    l.sort()
    val=" "
    for item in l:
        if item == val:
            l.remove(item)
        val=item
    return l

def getMaxOccurrence(l):
    max=0
    for item in l:
        if l.count(item) > max:
            max = l.count(item)
            val = item
    return val

def getMaxProduct(l):
    l.sort()

    if len(l) >= 3:
        val = l[-1]*l[-2]*l[-3]
    elif len(l) == 2:
        val = l[0]*l[1]
    else:
        val = l[0]
    return val

if __name__ == '__main__':
    result = removeDuplicates([1,1,1,2,3,4])
    print(result)