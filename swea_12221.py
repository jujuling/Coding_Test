T=int(input())

for test_case in range(1,T+1):
    a,b=map(int,input().split())
    if a<=9 and b<=9:
        print("#%d %d" %(test_case,a*b))
    else:
        print("#%d %d" %(test_case,-1))