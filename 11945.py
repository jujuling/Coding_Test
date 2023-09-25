import sys

n,m=map(int,sys.stdin.readline().split())

l=[]
for i in range(n):
    l.append(sys.stdin.readline().strip())

for i in range(n):
    print(l[i][::-1])