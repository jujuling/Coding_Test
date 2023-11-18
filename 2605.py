from collections import deque
import sys

n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
j=deque()

for i in range(len(l)):
    if l[i]==0:
        j.append(i+1)
    else:
        j.insert(len(j)-l[i],i+1)

for i in j:
    print(i,end=' ')