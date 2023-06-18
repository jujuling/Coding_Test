import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

a=list(set(a))
a.sort()
for i in a:
    print(i,end=' ')