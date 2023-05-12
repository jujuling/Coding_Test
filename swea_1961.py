T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    a=list()
    for i in range(n):
        a.append(list(map(int,input().split())))
    print("#%d" %test_case)

    for i in range(n):
        # 90도
        for j in range(n):
            print(a[n-1-j][i],end='')
        print(end=' ')
        # 180도
        for j in range(n):
            print(a[n-1-i][n-1-j],end='')
        print(end=' ')
        #270도
        for j in range(n):
            print(a[j][n-1-i],end='')
        print()