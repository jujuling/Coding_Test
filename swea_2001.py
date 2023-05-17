T=int(input())

for test_case in range(1,T+1):
    n,m=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(n)]

    maxn=0
    #i와 j 인덱스는 m*m 박스가 움직이는 것
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            #k와 l 인덱스는 m*m 박스 안의 요소들을 더하기 위해 사용
            for k in range(m):
                for l in range(m):
                    total += a[i+k][j+l]
                    if total>maxn:
                        maxn=total
    print("#%d %d" %(test_case,maxn))