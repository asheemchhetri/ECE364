#! /bin/bash
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$
exec 3<$1
exec 4>first10.txt
for (( i=1; i <= 10; i++)) 
do
    read line<&3
    echo $line>&4
    if (( i>5 ))
    then
        echo $line
    fi
done

exit 0
