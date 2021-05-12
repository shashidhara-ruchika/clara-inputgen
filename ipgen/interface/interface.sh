#!/bin/bash
FILE="$1"
FILE2="$2"
NEG="$3"
FUNC="$4"
COM="$5"
neg1=0
neg2=1
if [[ ! -f $FILE ]] && [[ ! -f $FILE2 ]] ; then
	echo "File does not exist"
	exit
fi
if [ -n $NEG ]; then
	if [ "$NEG" != "$neg1" ] && [ "$NEG" != "$neg2" ]; then
		echo "Incorrect flag type, use '0' or '1'"
		exit 1
	else 
		if [ "${FILE##*.}" == "c" ]; then
			if [ "${FILE##*.}" == "c" ]; then
				cat $FILE > sampleCode1.c
				python3 parser.py sampleCode1.c $NEG
				> concatOut.txt
				mkdir randImp
				mv sampleCode1.c randImp
				mv outputGen.py randImp
				mv concatOut.txt randImp
				cd randImp
				../../bin/crestc sampleCode1.c 2> outFile.txt
				../../bin/run_crest ./sampleCode1 10 -random_input
				python3 outputGen.py 9
				mv outputGen.py ..
				mv concatOut.txt ..
				mv sampleCode1.c ..
				cd ..
				mkdir dfsTact
				mv sampleCode1.c dfsTact
				mv outputGen.py dfsTact
				mv concatOut.txt dfsTact
				cd dfsTact
				../../bin/crestc sampleCode1.c 2> outFile.txt
				../../bin/run_crest ./sampleCode1 10 -dfs
				python3 outputGen.py 1
				mv outputGen.py ..
				mv concatOut.txt ..
				mv sampleCode1.c ..
				cd ..
				rm -R randImp
				rm -R dfsTact
			else 
				echo "Incorrect file match"
				exit 2
			fi
		
	
		elif [ "${FILE##*.}" == "py" ]; then
			if [ "${FILE##*.}" == "py" ]; then
				python3 gen_covgen.py $FILE
			else echo "Incorrect file match"
			fi
		else 
			echo "Incorrect File type"
			exit 3
		fi
	fi
fi
coms1=M
coms2=m
coms3=R
coms4=r
if [ $COM == $coms1 ]; then
	echo "Matching..."
	python3 claraComs.py $FILE $FILE2 match $FUNC
elif [ $COM == $coms2 ]; then
	echo "Matching..."
	python3 claraComs.py $FILE $FILE2 match $FUNC
elif [ $COM == $coms3 ]; then
	echo "Repairing..."
	python3 claraComs.py $FILE $FILE2 repair $FUNC
elif [ $COM == $coms4 ]; then
	echo "Repairing..."
	python3 claraComs.py $FILE $FILE2 repair $FUNC
else echo "Incorrect flag, use M to check for a correct match and R for repair function"
fi 




 
