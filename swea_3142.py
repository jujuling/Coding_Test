T=int(input())

for test_case in range(1,T+1):
    n,m=map(int,input().split())

    twin=0
    while n!=0:
        if twin+n==m:
            break
        else:
            n-=2
            twin+=1
    print("#%d %d %d" %(test_case,n,twin))