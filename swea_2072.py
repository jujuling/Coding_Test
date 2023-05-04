T=int(input())

for test_case in range(1,T+1):
    result=0
    list1=list(map(int,input().split()))

    for i in list1:
        if int(i)%2!=0:
            result +=int(i)
    print("#%d %d" %(test_case,result))