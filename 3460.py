import sys

t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    l=[]
    while n!=0:
        l.append(n%2)
        n//=2
    for j in range(len(l)):
        if l[j]==1:
            print(j,end=' ')