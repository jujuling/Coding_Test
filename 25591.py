import sys

l=list(sys.stdin.readline().split())

a=100-int(l[0])
b=100-int(l[1])
c=100-(a+b)
d=a*b
q=d//100
r=d%100

print(a,b,c,d,q,r)
if d>99:
    print(c+q,r)
else:
    print(c,d)