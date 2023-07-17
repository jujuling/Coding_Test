import sys
from collections import deque

n=int(sys.stdin.readline())
l=deque(range(1,n+1))
while len(l)!=1:
    l.popleft()
    if len(l)==1:
        break
    tmp=l[0]
    l.popleft()
    l.append(tmp)
print(l[0])