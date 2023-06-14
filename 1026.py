import sys
n=int(sys.stdin.readline())

a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

a.sort()
result=0
for i in range(n):
    maxb=max(b)
    idx=b.index(maxb)
    result+=maxb*a[i]
    b[idx]=-1
print(result)
