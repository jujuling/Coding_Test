T=int(input())
days=[31,28,31,30,31,30,31,31,30,31,30,31]
for test_case in range(1,T+1):
    m1,d1,m2,d2 = map(int,input().split())
    result=0
    hap1=0
    hap2=0
    for i in range(m1-1):
        hap1+=days[i]
    hap1+=d1
    for i in range(m2-1):
        hap2+=days[i]
    hap2+=d2
    result=hap2-hap1+1
    print("#%d %d" %(test_case,result))