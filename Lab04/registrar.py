import glob
import os
def getDetails():
    with open("files/students.txt","r") as file:
        all_lines = file.readlines()
        student={}
        details={}
        for line in all_lines[2:]:
            student.update({line.split()[4] : line.split()[0]+" "+line.split()[1]+" "+line.split()[2]})
        filelist = glob.glob('files/EECS*')
        for filename in filelist:
            course = filename.strip("'files/EECS' '.txt'")
            with open(filename,"r") as file1:
                all_lines1 = file1.readlines()
                for line1 in all_lines1[2:]:
                    name = student[line1.split()[0]]
                    score = int(line1.split()[1])
                    if  not details or name not in details.keys():
                        details.update({name:{(course, score)}})
                    else:
                        details[name].add((course, score))
    return details


def getStudentList(course):
    with open("files/students.txt","r") as file:
        all_lines = file.readlines()
        student={}
        val=[]
        for line in all_lines[2:]:
            student.update({line.split()[4] : line.split()[0]+" "+line.split()[1]+" "+line.split()[2]})
        if not os.path.exists("files/EECS"+str(course)+".txt"):
            return val
        else:
            with open("files/EECS"+str(course)+".txt","r") as file1:
                all_lines1 = file1.readlines()
                for line1 in all_lines1[2:]:
                    name = student[line1.split()[0]]
                    val.append(name)
        val.sort()

    return val

def searchForName(name):
    with open("files/students.txt","r") as file:
        all_lines = file.readlines()
        student={}
        val={}
        for line in all_lines[2:]:
            student.update({line.split()[0]+" "+line.split()[1]+" "+line.split()[2]:line.split()[4] })
    if name not in student.keys():
        return val
    filelist = glob.glob('files/EECS*')
    for filename in filelist:
        course = filename.strip("'files/EECS' '.txt'")
        with open(filename,"r") as file1:
            all_lines1 = file1.readlines()
            for line1 in all_lines1[2:]:
                if student[name] == line1.split()[0]:
                    val.update({course:int(line1.split()[1])})
    return val

def searchForID(id):
    with open("files/students.txt","r") as file:
        all_lines = file.readlines()
        student={}
        val={}
        for line in all_lines[2:]:
            student.update({line.split()[4] : line.split()[4]})
    if id not in student.keys():
        return val
    filelist = glob.glob('files/EECS*')
    for filename in filelist:
        course = filename.strip("'files/EECS' '.txt'")
        with open(filename,"r") as file1:
            all_lines1 = file1.readlines()
            for line1 in all_lines1[2:]:
                if student[id] == line1.split()[0]:
                    val.update({course:int(line1.split()[1])})
    return val

def findScore(name, course):
    with open("files/students.txt","r") as file:
        all_lines = file.readlines()
        student={}
        for line in all_lines[2:]:
            student.update({line.split()[0]+" "+line.split()[1]+" "+line.split()[2]:line.split()[4] })
    filelist = glob.glob('files/EECS*')
    if name not in student.keys():
        return None
    for filename in filelist:
        coursenum = filename.strip("'files/EECS' '.txt'")
        if coursenum == course:
            with open(filename,"r") as file1:
                all_lines1 = file1.readlines()
                for line1 in all_lines1[2:]:
                    if student[name] == line1.split()[0]:
                        return int(line1.split()[1])
    return None

def getHighest(coursenum):
    maxnum=0
    name1=""
    studentlist=getStudentList(coursenum)
    if not studentlist:
        return ()
    for student in studentlist:
        score1=findScore(student,coursenum)
        if score1 > maxnum:
            maxnum=score1
            name1=student
    return(name1,float(maxnum))
def getLowest(coursenum):
    minnum=100
    name2=""
    studentlist=getStudentList(coursenum)
    if not studentlist:
        return ()
    for student in studentlist:
        score2=findScore(student,coursenum)
        if score2 < minnum:
            minnum=score2
            name2=student
    return(name2,float(minnum))

def getAverageScore(student):
    dic=searchForName(student)
    sum=0
    if not dic:
        return None
    for value in dic.values():
        sum+=value
    return sum/len(dic)

if __name__ == '__main__':
    from pprint import pprint as pp
    pp(searchForName("Martha E Garcia"))
