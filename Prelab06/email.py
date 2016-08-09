#! /usr/bin/env python3.4
#
#$Author: ee364b06 $
#$Date: 2016-02-21 18:48:20 -0500 (Sun, 21 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab06/email.py $
#$Revision: 88517 $

import re
import sys
def email(filename):
    with open(filename,"r") as file:
        lines=file.readlines()
        for line in lines:
            address=re.sub(r"@[\w.]+","@ecn.purdue.edu",line.split()[0])
            score=re.sub(r"\d+\.\d+",line.split()[1]+"/100",line.split()[1])
            print(address+"\t\t"+score)
if __name__ == '__main__':
    email(sys.argv[1])