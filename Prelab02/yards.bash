#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-24 16:27:32 -0500 (Sun, 24 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab02/yards.bash $
#$Revision: 86592 $
avg=0
var=0
max=0
if (( $# != 1 ))
then
    echo 'Usage: yards.bash <filename>'
    exit 1
else
    if [[ ! -e $1 || ! -r $1 ]]
    then
        echo "Error: $1 is not readable"
	exit 1
    else
        exec 3< $1
        while read line <&3
        do
	    arr=($line)
	    avg=0
	    var=0
            for (( i=1; i<${#arr[*]};i++ ))
	    do
		(( avg=$avg+${arr[i]} ))
	    done
	    ((avg=$avg/(${#arr[*]}-1)))
	    for (( i=1; i<${#arr[*]};i++ ))
	    do
		((var=(${arr[i]}-$avg)**2+$var))
	    done 
	    ((var=$var/(${#arr[*]}-1)))
	    echo "${arr[0]} schools averaged $avg yards receiving with a variance of $var"
	    if (( $avg > $max ))
	    then
		max=$avg
	    fi
	done
	echo "The largest average yardage was $max"
    fi
fi

exit 0
