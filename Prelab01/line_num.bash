#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-17 20:33:32 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab01/line_num.bash $
#$Revision: 85399 $

Num_Of_Param=$#
Param_Values=$@
cnt=1
content=1
if ((Num_Of_Param==1))
then
if [[ -e  $1 ]] && [[ -r $1 ]]
then
    while read content
    do
        echo "$cnt:$content"
        let cnt=$cnt+1
    done <$1
else
    echo "Cannot read $Param_Values" 
fi
else
    echo "Usage: line_num.bash <filename>"
fi
exit 0
