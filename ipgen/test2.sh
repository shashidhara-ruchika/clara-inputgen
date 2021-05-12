echo
echo Test2 - Checking whether a number is a palindrome
echo
cd clara
echo Correct Implementation ...
echo
cat -n example/t1pr.py
echo
echo Incorrect Implementation ...
echo
cat -n example/t1pi.py
echo
echo Running repairs on the program without IpGen ...
echo
echo clara repair example/t1pr.py example/t1pi.py --entryfnc palindrome --args "[[10]]" --ignoreio 1
echo
clara repair example/t1pr.py example/t1pi.py --entryfnc palindrome --args "[[10]]" --ignoreio 1
echo
echo
cd ..
cd crest/interface
echo Running repairs on the program after IpGen ...
echo
echo ./interface.sh t1pr.c t1pi.c 0 plaindrome R
echo
./interface.sh t1pr.py t1pi.py 0 palindrome R
echo
echo Contents of the Input Generated File ...
echo
cat concatOut.txt
echo 
echo
