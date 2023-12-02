import sys

n,k=map(int,sys.stdin.readline().split())
l=[1]
for i in range(2,n):
    if n%i==0:
        l.append(i)
l.append(n)

if k>len(l):
    print(0)
else:
    print(l[k-1])