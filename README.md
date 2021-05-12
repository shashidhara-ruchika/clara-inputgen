# clara-inputgen

Input Generation for CLARA (IpGen)

With the current global need for providing online learning over MOOC platforms, the need arises for being able to evaluate and correct introductory programming assignments in large numbers and provide personalized feedback on incorrect solutions to students. The tool CLARA is designed for such a purpose, and it requires a set of comprehensive input cases to generate corrections and give feedback on incorrect program codes, as it uses these inputs to generate a complete trace of the program.

The aim of this project is to create an input generator such that, given a program, generates input tests for it, in a manner consistent with the number and type of inputs accepted by the program, while covering all the conditional branches in the code. The requirement of maximum branch coverage is especially important for CLARA to generate the trace of the program as if any branch is not covered, it might lead to that branch of the program never being evaluated by CLARA.

IpGen uses two tools, CREST and Covgen to generate inputs for C and Python programs repectively.

CREST is a concolic execution engine that combines symbolic and concrete execution for generating inputs. The tool uses DFS and Random strategies to select alternate branch and solve the modified path constraints to generate inputs corresponding to this alternate branch. A given program written in C must first be compatible with the CREST tool to generate inputs for it. Using the help of AST and pycparser, a copy of the C program is modified and is passed into CREST to generate its own control flow graphs and generate inputs.

Covgen is a Python module available on the open source Python Package Index, that is used to generate test cases for Python programs. In contrast to the concolic search strategies used by CREST for C programs, Covgen utilizes a search-based test strategy. A given program written in Python must first be compatible with Covgen to generate inputs for it. Using the help of AST, a copy of the C program is modified and is passed into Covgen to generate its own control flow graphs and generate inputs.

The interface is the part of the program that allows the final user to generate inputs for the relevant program without having to worry about which implementation needs to be called based on the file type. The interface takes the following arguments:
1) The filename of the implementation containing the correct code
2) The filename of the implementation containing the incorrect code that is to be
corrected/on which feedback is to be generated
3) A binary value (0 or 1) that determines whether the user wishes negative numbers to be
generated as possible inputs
4) The name of the function that needs to be corrected in the feedback for it to be matched or repaired by CLARA
5) A single character determining the type of operation to be performed by CLARA (match/repair)
./interface.sh <correct-version-file> <incorrect-version-file> <positive/negative-flag> <function-name> <match/repair-flag>



Instructions to use IpGen inside Docker container interface

Clone/download the following repositories
git clone https://github.com/iradicek/clara.git
git clone https://github.com/sosy-lab/crest.git

Download and unzip yices 1.0.40 and place it inside crest/src
Change YICES_DIR to point to yices-1.0.40 inside Makefile

Place the inteface directory inside crest

Place the example directory inside clara

Install Docker

Build the docker image for ipgen
docker build . --rm=true -t <image-name>
docker build . --rm=true -t ipgen

Start the image
docker run -ti --name <container-name> /bin/bash
docker run -ti --name ipgen_clara ipgen /bin/bash


To run examples present inside the newly created docker container

Invoke the interface to recieve feedback for matching a repairing of function gr in tpr.py(correct version) and tpi.py(incorrect version)
./interface.sh tpr.py tpi.py 0 gr M
./interface.sh tpr.py tpi.py 0 gr R

Invoke the interface to recieve feedback for matching a repairing of function largest_num in tcr.c(correct version) and tci.c(incorrect version)
./interface.sh tcr.c tci.c 0 largest_num M
./interface.sh tcr.c tci.c 0 largest_num R

View the inputs generagted for the most recent feedback
cat concatOut.txt


To run examples present inside examples directory

Place the correct and incorrect versions of the C or Python files to find inputs, matches, repairs etc.

Start the ipgen_clara container
docker start ipgen_clara

Copy the tr.c(correct version) and ti.c(incorrect version) into the container
docker cp examples/tr.c ipgen_clara:/root/ipgen/crest/interface
docker cp examples/ti.c ipgen_clara:/root/ipgen/crest/interface

Invoke the interface to recieve feedback for matching a repairing of function largest_num in tcr.c(correct version) and tci.c(incorrect version)
docker exec ipgen_clara ./interface.sh tr.c ti.c 0 largest_num M
docker exec ipgen_clara ./interface.sh tr.c ti.c 0 largest_num R

Copy the tr.py(correct version) and ti.py(incorrect version) into the container
docker cp examples/tr.py ipgen_clara:/root/ipgen/crest/interface
docker cp examples/ti.py ipgen_clara:/root/ipgen/crest/interface

Invoke the interface to recieve feedback for matching a repairing of function gr in tpr.py(correct version) and tpi.py(incorrect version)
docker exec ipgen_clara ./interface.sh tr.py ti.py 0 l3n M
docker exec ipgen_clara ./interface.sh tr.py ti.py 0 l3n R

View the inputs generagted for the most recent feedback
docker exec ipgen_clara cat concatOut.txt

To run automated tested examples
cd /root/ipgen

Test1 - Returning the largest of 3 numbers
./test1.sh

Test2 - Checking whether a number is a palindrome 
./test2.sh

Stop the ipgen_clara container
docker stop ipgen_clara


Other useful docker commands

To build the docker image for clara
docker build . --rm=true -t <image-name> 

To start the image (this command will take you inside this conatiner)
docker run -ti --name <container-name> <image-name>

To execute a any command inside this container
docker exec <container-name> <command>

To stop a container
docker stop <container-name>

To start a stopped container
docker start <container-name>

To copy a file into a container
docker cp <path-to-file> <container-name>:<path-inside-container>



Instructions to use IpGen on your system

Clone/download the following repositories
cd ipgen
git clone https://github.com/iradicek/clara.git
git clone https://github.com/sosy-lab/crest.git

Install the following packages for CLARA
sudo apt-get install cython
sudo apt-get install lp-solve liblpsolve55-dev

Install the following packages for CREST
sudo apt-get install ocaml
sudo apt-get install ocamlbuild
sudo apt-get install ocaml-findlib
sudo apt-get install mime-support

Install the following packages for Covgen
pip3 install astor
pip3 install anytree
pip3 install covgen

Download and unzip yices 1.0.40 and place it inside crest/src
Change YICES_DIR to point to yices-1.0.40 inside Makefile

Export the path to run CLARA
export LD_LIBRARY_PATH=/usr/lib/lp_solve/

Run and configure CLARA
cd clara
make

Run and configure CREST
cd crest/cil
./configure
make -pie
cd crest/src
make -pie

Give permission to invoke the interface
cd crest/interface
chmod 777 interface.sh

To run examples, place the correct and incorrect versions of the C or Python files to find inputs, matches, repairs etc. inside crest/interface
cd crest/interface

Invoke the interface to recieve feedback for matching a repairing of function gr in tpr.py(correct version) and tpi.py(incorrect version)
./interface.sh tpr.py tpi.py 0 gr M
./interface.sh tpr.py tpi.py 0 gr R

Invoke the interface to recieve feedback for matching a repairing of function largest_num in tcr.c(correct version) and tci.c(incorrect version)
./interface.sh tcr.c tci.c 0 largest_num M
./interface.sh tcr.c tci.c 0 largest_num R

View the inputs generagted for the most recent feedback
cat concatOut.txt




