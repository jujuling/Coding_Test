import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
d=int(sys.stdin.readline())
e=int(sys.stdin.readline())
result=0

if a<0:
    result=(0-a)*c
    a=0
if a==0:
    result+=d
if a<=b:
    result+=(b-a)*e

print(result)