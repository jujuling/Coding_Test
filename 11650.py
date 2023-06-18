import sys

n=int(sys.stdin.readline())
x=[]
for i in range(n):
    tmp=list(map(int, sys.stdin.readline().split()))
    x.append(tmp)

x.sort()

for i in range(n):
    print(x[i][0],x[i][1])