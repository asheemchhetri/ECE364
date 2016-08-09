#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-25 00:50:36 -0500 (Mon, 25 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab02/process_temps.bash $
#$Revision: 86678 $
if (( $# != 1 ))
then
    echo 'Usage: process_temps.bash <input file>'
    exit 1
else
    if [[ ! -e $1 || ! -r $1 ]]
    then
        echo "Error: $1 is not a readable file"
	exit 2
    else
	exec 3<$1
	read line <&3
	while read line <&3
	do
	    avg=0
	    arr=($line)
	    for content in  ${arr[*]}
	    do
		(( avg=$avg+$content ))
	    done
	    (( avg=($avg-${arr[0]})/(${#arr[*]}-1) ))
	    echo "Average temprature for time ${arr[0]} was $avg C."
	    
	done
    fi
fi

exit 0