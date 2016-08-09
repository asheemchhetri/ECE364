#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-18 21:55:25 -0500 (Mon, 18 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab01/sensor_sum.sh $
#$Revision: 85938 $

Num_Of_Param=$#
Param_Values=$@
curr=1
sum=0
if ((Num_Of_Param==1))
then
if [[ -e  $1 ]] && [[ -r $1 ]]
then
    while read content
    do
        let sum=$(echo $content | cut -f 2 -d ' ')+$(echo $content | cut -f 3 -d ' ')+$(echo $content | cut -f 4 -d ' ' )
    echo "$(echo $content | cut -f 1 -d "-" )"" ""$sum"
    done<$1
else
    echo "Cannot read $Param_Values" 
fi
else
    echo "Usage: ./sensor_sum.sh <filename>"
fi
exit 0
