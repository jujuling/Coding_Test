import sys

l=int(sys.stdin.readline())
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
d=int(sys.stdin.readline())

korean=0
math=0

if a%c==0:
    korean=a//c
else:
    korean=a//c+1
if b%d==0:
    math=b//d
else:
    math=b//d+1

result=l-max(korean,math)
print(result)