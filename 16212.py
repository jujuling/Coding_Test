import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

a.sort()
for i in a:
    print(i,end=' ')