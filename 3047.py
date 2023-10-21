import sys

l=list(map(int,sys.stdin.readline().split()))
l.sort()
a=l[0]
b=l[1]
c=l[2]
string=list(sys.stdin.readline().strip())

for i in string:
    if i=='A':
        print(a,end=' ')
    elif i=='B':
        print(b,end=' ')
    else:
        print(c,end=' ')