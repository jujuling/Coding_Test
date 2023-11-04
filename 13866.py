import sys

l = list(map(int,sys.stdin.readline().split()))

t1=l[0]+l[3]
t2=l[1]+l[2]

print(abs(t1-t2))