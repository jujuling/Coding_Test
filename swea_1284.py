T=int(input())

for test_case in range(1,T+1):
    p,q,r,s,w=map(int,input().split())
    a=0
    b=0
    #a 요금
    a=p*w

    #b 요금
    if w<=r:
        b=q
    else:
        w-=r
        b=w*s+q

    print("#%d %d" %(test_case,min(a,b)))