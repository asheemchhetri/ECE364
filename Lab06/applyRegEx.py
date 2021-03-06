#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-02-23 15:08:15 -0500 (Tue, 23 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Lab06/applyRegEx.py $
#$Revision: 88743 $

import re
def getRejectedUsers():
    l=[]
    with open("SiteRegistration.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            m=re.match(r"(?P<name>[a-zA-Z]+\,?\s[a-zA-Z]+)",line)
            m1=re.search(r"(?P<email>[\w_.-]+@[\w_.-]+)",line)
            m2=re.search(r"(?P<phone>\(?\d\d\d\)?\s?\-?\d\d\d\-?\d\d\d\d)",line)
            m3=re.search(r"(?P<state>,,[a-zA-Z]+\s?[a-zA-Z]+)",line)
            if m:
                if not m1 and not m2 and not m3:
                    name = m.group("name")
                    m4=re.match(r"([a-zA-Z]+)\,\s([a-zA-Z]+)",name)
                    if m4:
                        name = m4.group(2)+" "+m4.group(1)
                    l.append(name)
    l.sort()
    return l

def getUsersWithEmails():
    val={}
    with open("SiteRegistration.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            m=re.match(r"(?P<name>[a-zA-Z]+\,?\s[a-zA-Z]+)",line)
            m1=re.search(r"(?P<email>[\w_.-]+@[\w_.-]+)",line)
            if m and m1:
                name = m.group("name")
                m4=re.match(r"([a-zA-Z]+)\,\s([a-zA-Z]+)",name)
                if m4:
                    name = m4.group(2)+" "+m4.group(1)
                val.update({name:m1.group("email")})
    return val

def getUsersWithPhones():
    val={}
    with open("SiteRegistration.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            m=re.match(r"(?P<name>[a-zA-Z]+\,?\s[a-zA-Z]+)",line)
            m1=re.search(r"\(?(\d\d\d)\)?\s?\-?(\d\d\d)\-?(\d\d\d\d)",line)
            if m and m1:
                name = m.group("name")
                m4=re.match(r"([a-zA-Z]+)\,\s([a-zA-Z]+)",name)
                if m4:
                    name = m4.group(2)+" "+m4.group(1)

                val.update({name:"("+m1.group(1)+") "+m1.group(2)+"-"+m1.group(3)})
    return val

def getUsersWithStates():
    val={}
    with open("SiteRegistration.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            m=re.match(r"(?P<name>[a-zA-Z]+\,?\s[a-zA-Z]+)",line)
            m1=re.findall(r"([A-Z][a-z]+)",line)
            if m and len(m1)>=3:
                name = m.group("name")
                m4=re.match(r"([a-zA-Z]+)\,\s([a-zA-Z]+)",name)
                if m4:
                    name = m4.group(2)+" "+m4.group(1)
                if(len(m1)==3):
                    val.update({name:m1[-1]})
                else:
                    val.update({name:m1[-2]+" "+m1[-1]})
    return val

def getUsersWithoutEmails():
    phones=getUsersWithPhones()
    states=getUsersWithStates()
    val=[]
    with open("SiteRegistration.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            m=re.match(r"(?P<name>[a-zA-Z]+\,?\s[a-zA-Z]+)",line)
            m1=re.search(r"(?P<email>[\w_.-]+@[\w_.-]+)",line)
            if m:
                name = m.group("name")
                m4=re.match(r"([a-zA-Z]+)\,\s([a-zA-Z]+)",name)
                if m4:
                    name = m4.group(2)+" "+m4.group(1)
                if (name in phones.keys() or name in states.keys()) and not m1:
                    val.append(name)
    val.sort()
    return val

def getUsersWithoutPhones():
    states=getUsersWithStates()
    emails=getUsersWithEmails()
    val=[]
    with open("SiteRegistration.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            m=re.match(r"(?P<name>[a-zA-Z]+\,?\s[a-zA-Z]+)",line)
            m1=re.search(r"\(?(\d\d\d)\)?\s?\-?(\d\d\d)\-?(\d\d\d\d)",line)
            if m:
                name = m.group("name")
                m4=re.match(r"([a-zA-Z]+)\,\s([a-zA-Z]+)",name)
                if m4:
                    name = m4.group(2)+" "+m4.group(1)
                if (name in states.keys() or name in emails.keys()) and not m1:
                    val.append(name)
    val.sort()
    return val

def getUsersWithoutStates():
    phones=getUsersWithPhones()
    emails=getUsersWithEmails()
    val=[]
    with open("SiteRegistration.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            m=re.match(r"(?P<name>[a-zA-Z]+\,?\s[a-zA-Z]+)",line)
            m1=re.findall(r"([A-Z][a-z]+)",line)
            if m:
                name = m.group("name")
                m4=re.match(r"([a-zA-Z]+)\,\s([a-zA-Z]+)",name)
                if m4:
                    name = m4.group(2)+" "+m4.group(1)
                if (name in phones.keys() or name in emails.keys()) and len(m1)<3:
                    val.append(name)
    val.sort()
    return val

def getUsersWithCompleteInfo():
    phones=getUsersWithPhones()
    emails=getUsersWithEmails()
    states=getUsersWithStates()
    val={}
    with open("SiteRegistration.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            m=re.match(r"(?P<name>[a-zA-Z]+\,?\s[a-zA-Z]+)",line)
            if m:
                name = m.group("name")
                m4=re.match(r"([a-zA-Z]+)\,\s([a-zA-Z]+)",name)
                if m4:
                    name = m4.group(2)+" "+m4.group(1)
                if (name in phones.keys() and name in emails.keys()) and name in states.keys():
                    val.update({name:(emails[name],phones[name],states[name])})

    return val



if __name__ == '__main__':
    print(getUsersWithoutEmails())