import sys

n=int(sys.stdin.readline())
sit=[0 for _ in range(101)]
l=list(map(int,sys.stdin.readline().split()))
result=0

for i in l:
    if sit[i]==0:
        sit[i]=1
    else:
        result += 1
print(result)