#! /bin/bash
#
#$Author: ee364b06 $
#$Date: 2016-02-01 12:53:41 -0500 (Mon, 01 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b06/Lab02/hangman.bash $
#$Revision: 87393 $
if (( $# != 0 ))
then
    echo 'Usage: hangman.bash'
    exit 1
else
    ((choice=$RANDOM%3))
    arr1=(b a n a n a)
    arr2=(p a r s i m o n i o u s)
    arr3=(s e s q u i p e d a l i a n)
    if (( $choice == 0 ))
    then
	echo "Your word is ${#arr1[*]} letters long."
        temp1=("." "." "." "." "." ".")
	echo "Word is: . . . . . ."
	check=0
	good=0
	while (( $check == 0 ))
	do
	    read -p "  Make a guess: " guess
	    good=0
	    for (( i=0; i<6; i++))
	    do
		if [[ $guess == ${arr1[i]} && ${temp1[i]} == "." ]]
		then
		    temp1[i]=$guess
		    good=1;
		fi
	    done
	    if(( good == 1 ))
	    then
		echo "  Good going!"
	    else
		echo "  Sorry, try again."
	    fi
	    echo 
	    if [[ ${temp1[*]} == ${arr1[*]} ]]
	    then
		check=1
		echo "Contratulation! You guessed the word: banana"
	    else
		echo "Word is: ${temp1[0]}  ${temp1[1]}  ${temp1[2]}  ${temp1[3]}  ${temp1[4]}  ${temp1[5]}"
	    fi
	  
	done
    fi
     if (( $choice == 1 ))
    then
	echo "Your word is ${#arr2[*]} letters long."
        temp2=("." "." "." "." "." "." "." "." "." "." "." ".")
	echo "Word is: . . . . . . . . . . . ."
	check=0
	good=0
	while (( $check == 0 ))
	do
	    read -p "  Make a guess: " guess
	    good=0
	    for (( i=0; i<12; i++))
	    do
		if [[ $guess == ${arr2[i]} && ${temp2[i]} == "." ]]
		then
		    temp2[i]=$guess
		    good=1;
		fi
	    done
	    if(( good == 1 ))
	    then
		echo "  Good going!"
	    else
		echo "  Sorry, try again."
	    fi
	    echo 
	    if [[ ${temp2[*]} == ${arr2[*]} ]]
	    then
		check=1
		echo "Contratulation! You guessed the word: parsimonious"
	    else
		echo "Word is: ${temp2[0]}  ${temp2[1]}  ${temp2[2]}  ${temp2[3]}  ${temp2[4]}  ${temp2[5]}  ${temp2[6]}  ${temp2[7]}  ${temp2[8]}  ${temp2[9]}  ${temp2[10]}  ${temp2[11]}"
	    fi
	  
	done
    fi
      if (( $choice == 2 ))
    then
	echo "Your word is ${#arr3[*]} letters long."
        temp3=("." "." "." "." "." "." "." "." "." "." "." "." "." ".")
	echo "Word is: . . . . . . . . . . . . . ."
	check=0
	good=0
	while (( $check == 0 ))
	do
	    read -p "  Make a guess: " guess
	    good=0
	    for (( i=0; i<14; i++))
	    do
		if [[ $guess == ${arr3[i]} && ${temp3[i]} == "." ]]
		then
		    temp3[i]=$guess
		    good=1;
		fi
	    done
	    if(( good == 1 ))
	    then
		echo "  Good going!"
	    else
		echo "  Sorry, try again."
	    fi
	    echo 
	    if [[ ${temp3[*]} == ${arr3[*]} ]]
	    then
		check=1
		echo "Contratulation! You guessed the word: sesquipedalian"
	    else
		echo "Word is: ${temp3[0]}  ${temp3[1]}  ${temp3[2]}  ${temp3[3]}  ${temp3[4]}  ${temp3[5]}  ${temp3[6]}  ${temp3[7]}  ${temp3[8]}  ${temp3[9]}  ${temp3[10]}  ${temp3[11]} ${temp3[12]} ${temp3[13]}"
	    fi
	  
	done
    fi
fi
 
