import sys

n=int(sys.stdin.readline())

k=1
result=0
while n!=0:
    if n<k:
        k=1
    n-=k
    result+=1
    k+=1
print(result)