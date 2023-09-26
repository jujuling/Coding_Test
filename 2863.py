import sys

a,b=map(int,sys.stdin.readline().split())
c,d=map(int,sys.stdin.readline().split())

l=[]
l.append(a/c+b/d)
l.append(c/d+a/b)
l.append(d/b+c/a)
l.append(b/a+d/c)

print(l.index(max(l)))