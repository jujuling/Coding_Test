import sys

n=int(sys.stdin.readline())
l=[]

for i in range(n):
    tmp=list(map(str,sys.stdin.readline().split()))
    l.append([tmp[0],int(tmp[1]),int(tmp[2]),int(tmp[3])])

l.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))

for i in range(n):
    print(l[i][0])