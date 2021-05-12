"""
import os
import sys
file = open("concatOut.txt","r")
count=0
for line in (file.read()).split("\n"):
	if line:
		count+=1
file.close()
f=open("concatOut.txt","r")
content=f.readlines()
inpt=0

while(inpt<len(content)):
	content[inpt]=[content[inpt].split()][0]
	ele="["
	trav=0
	while(trav<len(content[inpt])):
		ele+=content[inpt][trav]
		if(trav!=len(content[inpt])-1):
			ele+=","
		trav+=1
	ele+="]"
	content[inpt]=ele
	inpt+=1
inpt=0

if (sys.argv[3]=="match"):
	while(inpt<len(content)-1):
	        if(str(sys.argv[4]) == "main"):
	                print(sys.argv[4])
	                cmd="clara match " + sys.argv[1] + " " +sys.argv[2] + " --args " + "[" + content[inpt] + "," + content[inpt+1]+ "] --ignoreio 1"
	        else:
	                cmd="clara match " + sys.argv[1] + " " +sys.argv[2] + " --entryfnc "+ sys.argv[4] +" --args " + "[" + content[inpt] + "," + content[inpt+1]+ "] --ignoreio 1"
	        #print(cmd)	        
	        os.system(cmd)
	        inpt+=1
	        print()
else:
	#cmd="clara repair "+sys.argv[1]+" "+sys.argv[2]+" --entryfnc " + sys.argv[4] + " --args "+"[["+content[0]+"]] --ignoreio 1"
	#os.system(cmd)
	while(inpt<len(content)-1):
	        if(str(sys.argv[4]) == "main"):
	                cmd="clara repair " + sys.argv[1] + " " +sys.argv[2] +" --args " + "[" + content[inpt] + "," + content[inpt+1]+ "] --ignoreio 1"
	        else:
	                cmd="clara repair " + sys.argv[1] + " " +sys.argv[2] + " --entryfnc "+ sys.argv[4] +" --args " + "[" + content[inpt] + "," + content[inpt+1]+ "] --ignoreio 1"
	        #print(cmd)	        
	        os.system(cmd)
	        inpt+=1
	        print()	
"""	        

import os
import sys
file = open("concatOut.txt","r")
count=0
for line in (file.read()).split("\n"):
	if line:
		count+=1
file.close()
f=open("concatOut.txt","r")
content=f.readlines()
inpt=0

while(inpt<len(content)):
	content[inpt]=[content[inpt].split()][0]
	ele="["
	trav=0
	while(trav<len(content[inpt])):
		ele+=content[inpt][trav]
		if(trav!=len(content[inpt])-1):
			ele+=","
		trav+=1
	ele+="]"
	content[inpt]=ele
	inpt+=1
#print(content)	
inpt=0
inputs=""
while(inpt<len(content)):
	inputs = inputs+content[inpt]+","
	inpt += 1
inputs=inputs[:-1]

if (sys.argv[3]=="match"):
        if(str(sys.argv[4]) == "main"):
                print(sys.argv[4])
                cmd="clara match " + sys.argv[1] + " " +sys.argv[2] + " --args " + "[" + inputs + "] --ignoreio 1"
        else:
                cmd="clara match " + sys.argv[1] + " " +sys.argv[2] + " --entryfnc "+ sys.argv[4] +" --args " + "[" + inputs + "] --ignoreio 1"
                os.system(cmd)
                print()
                
else:
        if(str(sys.argv[4]) == "main"):
                cmd="clara repair " + sys.argv[1] + " " +sys.argv[2] +" --args " + "[" + inputs + "] --ignoreio 1"
        else:
                cmd="clara repair " + sys.argv[1] + " " +sys.argv[2] + " --entryfnc "+ sys.argv[4] +" --args " + "[" + inputs + "] --ignoreio 1"
                os.system(cmd)
                print()	
