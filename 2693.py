import sys

t=int(sys.stdin.readline())

for i in range(t):
    l=list(map(int,sys.stdin.readline().split()))
    l.sort()
    print(l[-3])