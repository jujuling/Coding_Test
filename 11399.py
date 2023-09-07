import sys

n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
t=[]
l.sort()

for i in range(n):
    tmp=0
    for j in range(i+1):
        tmp+=l[j]
    t.append(tmp)

print(sum(t))