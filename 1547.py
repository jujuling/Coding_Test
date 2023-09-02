import sys

m=int(sys.stdin.readline())
l=[1,0,0]
for i in range(m):
    x,y=map(int,sys.stdin.readline().split())
    x-=1
    y-=1
    tmp=l[x]
    l[x]=l[y]
    l[y]=tmp

print(l.index(1)+1)