import sys

n=int(sys.stdin.readline())
d=[0]*(n+1)
if n==0:
    print(0)
elif n<3:
    print(1)
else:
    d[1]=1
    d[2]=1

    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    print(d[n])