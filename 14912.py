import sys

n,d=map(int,sys.stdin.readline().split())
l=[i for i in range(1,n+1)]
result=0
for i in range(n):
    result+=(str(l[i]).count(str(d)))
print(result)