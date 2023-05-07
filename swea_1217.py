def re(n,m):
    if m>1:
        return n*re(n,m-1)
    else:
        return n
for i in range(10):
    index=int(input())
    n,m =map(int,input().split())
    print("#%d %d" %(index,re(n,m)))