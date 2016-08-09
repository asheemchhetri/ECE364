#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-25 00:49:50 -0500 (Mon, 25 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab02/run.bash $
#$Revision: 86677 $
if (( $# != 2 ))
then
    echo 'Usage: run.bash <simulation code> <output file>'
    exit 1
else
    if [[ ! -e $1 || ! -r $1 ]]
    then
        echo "Error: $1 is not readable"
	exit 1
    else
	if [[ -e "quick_sim" ]]
	then
	    rm quick_sim
	fi

	gcc $1 -o quick_sim

	if (( $? != 0 ))
	then 
	    echo "error: quick_sim could not be compiled!"
	    exit 1
	fi
	filename=$2
	if [[ -e $2 ]]
	then
	    read -p "$2 exists. Would you like to delete it?" check
            if [[ $check == "yes" || $check == "y" ]]
	    then
		rm $2
	    elif [[ $check == "no" || $check == "n" ]]
	    then
		read -p "Enter a new filename: " filename
	    fi
	
	fi
	arr1=(1 2 4 8 16 32)
	arr2=(1 2 4 8 16)
	min=9999999
	for i in ${arr1[*]}
	do
	    for j in ${arr2[*]}
	    do
	
		cpitt=$(quick_sim $i $j a | cut -f 8,10 -d ':')
		cpi=$(echo $cpitt | cut -f 1 -d ':')
		tt=$(echo $cpitt | cut -f 2 -d ':')
		if (( $tt < $min ))
		then
		    min=$tt
		    name="AMD Opteron"
		    cs=$i
		    iw=$j
		fi
		echo "AMD Opteron:$i:$j:$cpi:$tt" >>$filename
		cpitt=($(quick_sim $i $j i | cut -f 8,10 -d ':'))
		cpi=$(echo $cpitt | cut -f 1 -d ':')
		tt=$(echo $cpitt | cut -f 2 -d ':')
		if (( $tt < $min ))
		then
		    min=$tt
		    name="Intel Core i7"
		    cs=$i
		    iw=$j
		fi
		echo "Intel Core i7:$i:$j:$cpi:$tt" >>$filename
	    done
	done
	echo "Fastest run time achieved by $name with cache size $cs and issue width $iw was $min"
    fi
fi

exit 0
	    