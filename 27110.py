import sys
n=int(sys.stdin.readline())
a,b,c=map(int,sys.stdin.readline().split())

result=0

if a>=n:
    result+=n
else:
    result+=a
if b >= n:
    result += n
else:
    result += b
if c >= n:
    result += n
else:
    result += c

print(result)