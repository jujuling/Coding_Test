T=int(input())

for test_case in range(1,T+1):
    n,a,b=map(int,input().split())
    maxn=0
    minn=0
    if a+b<=n:
        maxn=min(a,b)
        minn=0
    elif a+b>n:
        maxn = min(a, b)
        minn = max(a,b)+min(a,b)-n
    print("#%d %d %d" %(test_case,maxn,minn))