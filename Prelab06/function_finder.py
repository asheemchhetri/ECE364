#! /usr/bin/env python3.4
#
#$Author: ee364b06 $
#$Date: 2016-02-21 18:49:33 -0500 (Sun, 21 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab06/function_finder.py $
#$Revision: 88519 $

import re
import sys
import os
def function_finder(filename):
    with open(filename,"r") as file:
        lines=file.readlines()
        for line in lines:
            function=re.match(r"def\s+([\w_-]+)\s*\(([\w\s=-_,]+)\)",line)
            if function:
                print(function.group(1))
                l=function.group(2).split(",")
                cnt=1
                for item in l:
                    print("Arg"+str(cnt)+": "+item.strip())
                    cnt+=1

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print("Usage: function_finder.py [python_file_name]")
    elif not os.access(sys.argv[1], os.R_OK):
        print("Error: Could not read "+sys.argv[1])
    else:
        function_finder(sys.argv[1])

