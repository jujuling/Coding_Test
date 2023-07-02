import sys

n,b=map(int,sys.stdin.readline().split())

l=[]

while n!=0:
    tmp=n%b
    l.append(tmp)
    n//=b
l.reverse()

for i in l:
    if i<10:
        print(i,end='')
    else:
        print(chr(i+55),end='')

