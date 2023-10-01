import sys

a,b=map(int,sys.stdin.readline().split())
l=[0]

for i in range(b+1):
    for j in range(i):
        l.append(i)

print(sum(l[a:b+1]))