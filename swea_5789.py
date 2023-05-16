T=int(input())

for test_case in range(1,T+1):
    n,q=map(int,input().split())
    a=[0 for _ in range(n)]
    for i in range(1,q+1):
        l,r=map(int,input().split())
        for j in range(l-1,r):
            a[j]=i
    print("#%d" %test_case, end=' ')
    for i in a:
        print(i,end=' ')
    print()