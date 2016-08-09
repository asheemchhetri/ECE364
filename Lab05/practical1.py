import glob
def rowSumIsValid(mat):
    pre=0
    for row in mat:
        curr=sum(row)
        if pre == 0:
            pre=curr
        if pre == curr:
            pre=curr
        else:
            return False

    return True

def columnSumIsValid(mat):
    size=len(mat[0])
    val=[0]*size
    for row in mat:
        i=0
        while i<size:
            val[i]+=row[i]
            i+=1
    cmp=val[0]
    for item in val:
        if not cmp == item:
            return False

    return True

def magicSquareIsValid(filePath):
    with open(filePath,"r") as file:
        all_lines = file.readlines()
        mat=[]
        for line in all_lines:
            l=[]
            for item in line.split():
                l.append(int(item))
            mat.append(l)
    if rowSumIsValid(mat) == True and columnSumIsValid(mat) == True:
        return True
    else:
        return False

def getTotalCost(itemSet):
    item={}
    for t in list(itemSet):
        item.update({t[0]:t[1]})

    cpu={}
    filelist = glob.glob('Stores/*.txt')
    for filename in filelist:
        store = filename.lstrip('Stores/')

        store = store[:-4]
        cpu.update({store:0})
        with open(filename,"r") as file:
            all_lines = file.readlines()
            for line in all_lines[3:]:
                for name in item.keys():
                    if name == line.split()[0]+" "+line.split()[1]:
                        cpu[store]+=item[name]*float(line.split()[3].strip("$"))
                        cpu[store]=round(cpu[store],2)

    return cpu

def getBestPrices(cpuSet):
    cpuSet=list(cpuSet)
    price={}
    for item in cpuSet:
        price.update({item:[999999999," "]})

    filelist = glob.glob('Stores/*.txt')
    for filename in filelist:
        store = filename.lstrip('Stores/')
        store = store[:-4]
        with open(filename,"r") as file:
            all_lines = file.readlines()
            for line in all_lines[3:]:
                for cpu in price.keys():
                   if cpu == line.split()[0]+" "+line.split()[1] and float(line.split()[3].strip("$")) < price[cpu][0]:
                       price[cpu][0]= float(line.split()[3].strip("$"))
                       price[cpu][1]= store

    for item in cpuSet:
        price[item]=tuple(price[item])

    return price

def getMissingItems():
    cpu={}
    mcpu={}
    filelist = glob.glob('Stores/*.txt')
    for filename in filelist:
        store = filename.lstrip('Stores/')
        store = store[:-4]
        cpu.update({store:[]})
        with open(filename,"r") as file:
            all_lines = file.readlines()
            for line in all_lines[3:]:
                cpu[store].append(line.split()[0]+" "+line.split()[1])
    for s in cpu.keys():
        mcpu.update({s:[]})
        for k in cpu.keys():
            for item in cpu[k]:
                if item not in cpu[s]:
                    mcpu[s].append(item)

    for key in mcpu.keys():
        mcpu[key] = set(mcpu[key])

    return mcpu




if __name__ == '__main__':
    print(getMissingItems())
