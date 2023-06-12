import sys
n=int(sys.stdin.readline())
nlist=[0]*10000

for _ in range(n):
    tmp=int(sys.stdin.readline())
    nlist[tmp-1]+=1

for i in range(10000):
    if nlist[i]!=0:
        for j in range(nlist[i]):
            print(i+1)