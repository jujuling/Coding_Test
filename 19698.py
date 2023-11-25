import sys

n,w,h,l=map(int,sys.stdin.readline().split())
a=w//l
b=h//l

if n>a*b:
    print(a*b)
else:
    print(n)