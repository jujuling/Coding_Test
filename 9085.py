import sys

t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    l=list(map(int,sys.stdin.readline().split()))
    print(sum(l))