echo
echo Test1 - Returning the largest of 3 numbers
echo
cd clara
echo Correct Implementation ...
echo
cat -n example/tcr.c
echo
echo Incorrect Implementation ...
echo
cat -n example/tci.c
echo 
echo Running repairs on the program without IpGen ...
echo
echo clara repair example/tcr.c example/tci.c --entryfnc largest_num --args "[[2,1,3]]" --ignoreio 1
echo
clara repair example/tcr.c example/tci.c --entryfnc largest_num --args "[[2,1,3]]" --ignoreio 1
echo 
echo
cd ..
cd crest/interface
echo Running repairs on the program after IpGen ...
echo
echo ./interface.sh tcr.c tci.c 0 largest_num R
echo
./interface.sh tcr.c tci.c 0 largest_num R
echo
echo Contents of the Input Generated File ...
echo
cat concatOut.txt
echo
echo
