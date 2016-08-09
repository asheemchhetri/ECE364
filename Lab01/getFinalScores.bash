#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-19 15:20:59 -0500 (Tue, 19 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Lab01/getFinalScores.bash $
#$Revision: 86199 $

if (( $# == 1 ))
then
    if [[ -e $1 ]] && [[ -r $1 ]]
    then
        if [[ ! -e $(echo $1 | cut -f 1 -d ".").out ]] 
        then
            while read content 
            do
                let sum=15*$(echo $content | cut -f 2 -d ',')/100+30*$(echo $content | cut -f 3 -d ',')/100+30*$(echo $content | cut -f 4 -d ',')/100+25*$(echo $content | cut -f 5 -d ',')/100
	        echo "$(echo $content | cut -f 1 -d ","),$sum" >>$(echo $1 | cut -f 1 -d ".").out 
        done<$1
	else
            echo "Output file$(echo $1 | cut -f 1 -d ".").out already exists."
	    exit 3
        fi	
    else
	echo "Error reading input file: $1"
	exit 2
    fi
else
echo "Usage: ./getFinalScores.bash $1"
fi
exit 0

