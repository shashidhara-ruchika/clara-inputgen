import sys
lim=int(sys.argv[1])
cnt=0;
file2=open('concatOut.txt','a')
file1=open('input','r')
l=file1.readlines()
out=' '.join([line.strip() for line in l])
file2.write(out)
file2.write('\n')
file1.close()
while (cnt<=lim):
	fname='input'+str(cnt)
	cnt+=1
	file3=open(fname,'r')
	l=file3.readlines()
	out=' '.join([line.strip() for line in l])
	file2.write(out)
	file2.write('\n')
	file3.close()
file2.close()
