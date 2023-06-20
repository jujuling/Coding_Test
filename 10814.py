import sys

n=int(sys.stdin.readline())
l=[]
for i in range(n):
    age,name=map(str,sys.stdin.readline().split())
    tmp=[]
    tmp.append(int(age))
    tmp.append(name)
    l.append(tmp)

l=sorted(l,key=lambda x:x[0])

for i in range(n):
    print(l[i][0],l[i][1])