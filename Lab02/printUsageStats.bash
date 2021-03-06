#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-02-01 13:06:06 -0500 (Mon, 01 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Lab02/printUsageStats.bash $
#$Revision: 87398 $
if (( $# != 1 ))
then
    echo 'Usage: printUsageStats.bash <input file>'
    exit 1
else
    if [[ ! -e $1 || ! -r $1 ]]
    then
        echo "Error: $1 is not a readable file"
	exit 2
    else
	exec 3<$1
	read line <&3 
	timestamp=$( echo $line | cut -f3 -d ' ' )
	echo "Parsing file \"$1\". Timestamp: $timestamp"
	echo "Your choice are:"
	echo "1) Active user IDs"
	echo "2) N Highest CPU usages"
	echo "3) N Highest mem usages"
	echo "4) Top 3 longest running processes"
	echo "5) All process by a specific user"
	echo "6) Exit"
    fi
    choice=0
    while(( $choice != 6 ))
    do
    read -p "Please enter your choice: " choice
    if (( choice == 1))
    then
	activeids=$(echo $line | cut -f8 -d " ")
	echo "Total number of active user IDs: $activeids"
       
    fi
    if (( choice == 2))
    then
	read -p "Enter a value for N: " value
	for ((i=0; i<6 ;i++))
	do
	    read line <&3
	done
	for ((i=0; i<$value ;i++))
	do
	    read line <&3
	    name=$(echo $line | cut -f2 -d " ")
	    cpu=$(echo $line | cut -f9 -d " ")
	    echo "User $name is utilizing CPU resources at $cpu%"
	done

    fi
    if (( choice == 3))
    then
	read -p "Enter a value for N: " value
	sort -r -n -k10,10 $1 >new
	exec 4<new
	read line <&4
	for ((i=0; i<$value ;i++))
	do
	    read line <&4
	    
	    name=$(echo $line | cut -f2 -d " ")
	    mem=$(echo $line | cut -f10 -d " ")
	    echo "User $name is utilizing mem resources at $mem%"
	done
	rm new

    fi
    if (( choice == 4))
    then
	sort -n -r -k11,11 $1 >new
	exec 4<new
	for ((i=0; i<3 ;i++))
	do
	    read line <&4
	    
	    pid=$(echo $line | cut -f1 -d " ")
	    cmd=$(echo $line | cut -f12 -d " ")
	    echo "PID:$pid, cmd: $cmd"
	done
	rm new

    fi
    if (( choice == 5))
    then
	read -p "Please enter a valid username: " username
	grep $username $1 >new
	
	if [[ $? != 0 ]]
	then
	    echo "No match found"
	else
	    exec 4<new
	    while read line <&4
	    do	
		cpu=$(echo $line | cut -f9 -d " ")
		cmd=$(echo $line | cut -f12 -d " ")
		echo "$cpu $cmd"
	    done
	fi
	rm new

    fi
    echo
    done
fi
exit 0