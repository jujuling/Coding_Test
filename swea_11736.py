T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    nlist=list(map(int,input().split()))
    result=0
    for i in range(1,n-1):
        if min(nlist[i-1],nlist[i],nlist[i+1])!=nlist[i] and max(nlist[i-1],nlist[i],nlist[i+1])!=nlist[i]:
            result+=1
    print("#%d %d" %(test_case,result))