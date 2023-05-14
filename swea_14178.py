T=int(input())

for test_case in range(1,T+1):
    n,d=map(int,input().split())
    flag=d*2+1
    result=0
    result=n//flag
    if n%flag!=0:
        result+=1
    print("#%d %d" %(test_case,result))