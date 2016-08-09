#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-17 18:27:53 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab01/exist.bash $
#$Revision: 85368 $

Num_Of_Param=$#
Param_Values=$@
sum=0
while (($Num_Of_Param > 0))
do
    if [[ -e  $1 ]] && [[ -r $1 ]]
    then
	echo "File $1 is readable!"
    else
        touch $1
    fi
    shift
    let Num_Of_Param=$Num_Of_Param-1
done
exit 0
