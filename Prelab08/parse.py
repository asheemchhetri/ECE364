#! /usr/bin/env python3.4
import sys

try:
    with open(sys.argv[1],"r") as file:
        lines=file.readlines()
        for line in lines:
            list=line.split()
            string=""
            string_list=[]
            sum=0
            cnt=0
            for item in list:
                try:
                    sum+=float(item)
                    cnt+=1
                except ValueError:
                    string_list.append(item)
            if cnt !=0:
                string+=str(format(sum/cnt,".3f"))+" "
            for item in string_list:
                string+=item+" "
            else:
                string=string[:-1]
            print(string)
except IndexError:
    print("Usage: parse.py [filename]")
except IOError:
    print("{} is not a readable file.".format(sys.argv[1]))







