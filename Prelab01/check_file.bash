#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-01-18 18:03:27 -0500 (Mon, 18 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Prelab01/check_file.bash $
#$Revision: 85674 $

Num_Of_Param=$#
Param_Values=$@
if ((Num_Of_Param==1))
then
if [[ -e  $1 ]]
then
	echo "$1 exists"
else
	echo "$1 does not exist"
fi
if [[ -d  $1 ]]
then
	echo "$1 is a directory"
else
	echo "$1 is not a directory"
fi
if [[ -f  $1 ]]
then
	echo "$1 is an ordinary file"
else
	echo "$1 is not an ordinary file"
fi
if [[ -r  $1 ]]
then
	echo "$1 is readable"
else
	echo "$1 is not readable"
fi
if [[ -w  $1 ]]
then
	echo "$1 is writable"
else
	echo "$1 is not writable"
fi
if [[ -x  $1 ]]
then
	echo "$1 is executable"
else
	echo "$1 is not executable"
fi
else
    echo "Usage: ./check_file.bash <filename>"
fi
exit 0
