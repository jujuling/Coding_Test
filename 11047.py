import sys

n,k=map(int,sys.stdin.readline().split())
nlist=[]
for i in range(n):
    nlist.append(int(sys.stdin.readline()))
result=0
for i in range(n):
    tmp=k//nlist[n-1-i]
    if tmp!=0:
        result+=tmp
    k%=nlist[n-1-i]
print(result)