import glob
import filecmp
def getWordFrequency():
    filelist = glob.glob('files/*.txt')
    A = {}
    for filename in filelist:
        with open(filename, 'r') as file:
            line = file.readline()
        for item in line.split():
            item = item.rstrip("',' '.'")
            if item in A.keys():
                A[item] += 1
            else:
                A.update({item:1})
    return (A)

def getDuplicates():
    filelist = glob.glob('files/*.txt')
    duplicates={}
    for file in filelist:
        filename=file.strip("'files/' '.txt'")
        if not duplicates:
            duplicates.update({filename:[filename]})
        else:
            for key in duplicates.keys():
                if filecmp.cmp(file, 'files/'+key+'.txt'):
                    duplicates[key].append(filename)
                    nf=0
                    break
                else:
                    nf=1
            if nf == 1:
                duplicates.update({filename:[filename]})
    for key in duplicates.keys():
        duplicates[key].sort()
        key = duplicates[key][0]
        with open('files/'+key+'.txt', 'r') as file:
            line = file.readline()
            l=[]
            for item in line.split():
                item=item.strip("'.' ','")
                l.append(item)
            l=set(l)
        duplicates[key] = (len(l),duplicates[key])


    return duplicates


def getPurchaseReport():
    with open("purchases/Item List.txt","r") as file:
        all_lines = file.readlines()
        price={}
        report={}
        for line in all_lines[2:]:
            price.update({line.split()[0]:(line.split()[1]).lstrip("$")})
        filelist = glob.glob('purchases/purchase_*.txt')
        for file1 in filelist:
            filename=int(file1.strip("'purchases/purchase_' '.txt'"))
            report.update({filename:0})
            with open(file1,"r") as file:
                all_lines = file.readlines()
                for line in all_lines[2:]:
                    report[filename]+=float(price[line.split()[0]])*float(line.split()[1])
                report[filename]=round(report[filename],2)
    return report
def getTotalSold():
    filelist = glob.glob('purchases/purchase_*.txt')
    total={}
    for file1 in filelist:
        with open(file1,"r") as file:
            all_lines = file.readlines()
            for line in all_lines[2:]:
                nf=1
                for key in total.keys():
                    if line.split()[0] == key:
                        total[key]+=int(line.split()[1])
                        nf=0
                        break
                    else:
                        nf=1
                if nf == 1:
                    total.update({line.split()[0]:int(line.split()[1])})

    return total

if __name__ == '__main__':
    from pprint import pprint as pp
    pp(getPurchaseReport())
