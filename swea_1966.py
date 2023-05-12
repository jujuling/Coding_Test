T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    nlist=list(map(int,input().split()))
    nlist.sort()
    print("#%d" % test_case, end=' ')
    for i in range(n):
        print(nlist[i],end=' ')
    print()