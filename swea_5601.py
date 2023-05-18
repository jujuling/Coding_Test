T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    print("#%d" % test_case, end=' ')
    for i in range(n):
        print("%d/%d" %(1,n),end=' ')
    print()