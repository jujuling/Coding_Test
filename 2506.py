import sys

n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
cnt=list(0 for i in range(n))

if l[0]==1:
    cnt[0]=1
else:
    cnt[0]=0

for i in range(1,n):
    if l[i]==0:
        cnt[i]=0
    else: #l[i]==1
        if l[i-1]==1:
            cnt[i]=cnt[i-1]+1
        else:
            cnt[i]=1
print(sum(cnt))