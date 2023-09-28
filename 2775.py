import sys

t=int(sys.stdin.readline())

for i in range(t):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    #층과 호를 둘 다 생각해줘야하므로 이중배열
    d = [[0 for i in range(n+1)]for _ in range(k+1)]

    #0층 값은 i호에 i명이 사니까 미리 값 초기화해줌
    for i in range(1,n+1):
        d[0][i]=i
    #i층 j호의 사는 사람의 수는 i-1층의 j사람의 수와 i층의 j-1의 수의 합
    for i in range(1,k+1):
        for j in range(1,n+1):
            d[i][j]=d[i][j-1]+d[i-1][j]
    print(d[k][n])