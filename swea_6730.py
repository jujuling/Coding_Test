T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    case = list(map(int,input().split()))
    high=0
    low=0
    cha=list()
    for i in range(1,n):
        cha.append(case[i]-case[i-1])

    if len(cha)==1:
        if cha[0]<0:
            high=0
            low=cha[0]
        else:
            high=cha[0]
            low=0
    else:
        high = max(cha)
        low = min(cha)
    print("#%d %d %d" %(test_case, high, -(low)))