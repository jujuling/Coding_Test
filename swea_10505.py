T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    listn=list(map(int,input().split()))
    avg=sum(listn)/n
    result=0
    for i in listn:
        if i<=avg:
            result+=1
    print("#%d %d" %(test_case,result))