import sys

min=list(map(int,sys.stdin.readline().split()))
man=list(map(int,sys.stdin.readline().split()))
s=sum(min)
t=sum(man)

if s>=t:
    print(s)
else:
    print(t)