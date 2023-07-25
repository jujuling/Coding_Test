import sys

n,k=map(int,sys.stdin.readline().split())
result=1
div=1
for i in range(k):
    result*=(n-i)
    div*=(i+1)
print(result//div)