import sys

t=int(sys.stdin.readline())

for i in range(t):
    s=int(sys.stdin.readline())
    result=s
    n=int(sys.stdin.readline())
    for j in range(n):
        q,p=map(int,sys.stdin.readline().split())
        result+=q*p
    print(result)