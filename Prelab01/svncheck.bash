#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-18 22:02:28 -0500 (Mon, 18 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab01/svncheck.bash $
#$Revision: 85953 $

Num_Of_Param=$#
Param_Values=$@

if ((Num_Of_Param==1))
then
    if [[ -e $1 ]] && [[ -r $1 ]]
    then
    while read content <&3
    do
    STATUS=$(svn status $content | head -c 1)
    if [[ ! -e $content ]]
    then
        echo "Error:File $content appears to not exist here or in svn"
        exit 0
    fi
    if [[  $STATUS == "" ]]
    then
        
        if [[ ! -x $content ]]
        then
            svn propset svn:executable ON $content
        fi
    else 
         if [[ ! -x $content ]]
         then
             echo "Would you like to make $content executable?[y/n]"
             read check
             if [[ $check == "y" ]]
             then
                 chmod +x $content
             fi
         fi
         if [[ ! $STATUS == "A" ]]
         then 
            svn add $content
        fi
    fi
    done 3<$1
    echo "Auto-committing code"
    svn commit
else
    echo "$1 is not a readable file!"
fi
else
    echo "Usage: svncheck.bash <filename>"
fi

exit 0
