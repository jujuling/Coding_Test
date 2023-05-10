T=int(input())

for test_case in range(1,T+1):
    a=list(map(int,input().split()))
    for i in range(len(a)) :
        if a[i]<40:
            a[i]=40
    print("#%d %d" %(test_case,sum(a)/5))