import sys

n=int(sys.stdin.readline())
l=[[-1]*100 for _ in range(100)]
result=0

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            l[j][k]=0

for r in range(100):
    result+=l[r].count(0)
print(result)