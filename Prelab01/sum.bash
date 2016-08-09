#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-17 17:49:46 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab01/sum.bash $
#$Revision: 85355 $

Num_Of_Param=$#
Param_Values=$@
sum=0
while (($Num_Of_Param > 0))
do
    let sum=$sum+$1
    let Num_Of_Param=$Num_Of_Param-1
    shift
done
echo "$sum"
exit 0
