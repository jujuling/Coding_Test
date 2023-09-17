import sys
#런타임에러를 해결하기 위한 리밋설정
sys.setrecursionlimit(10**6)
def dfs(x,y):
    #상하좌우를 살피기 위함
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<m) and (0<=ny<n):
            #주변에 배추가 있다면 그 배추또한 0으로 변경하는 과정
            if graph[ny][nx]==1:
                graph[ny][nx]=0
                dfs(nx,ny)

t=int(sys.stdin.readline())
for i in range(t):
    result=0 #배추흰지렁이 수 저장할 변수
    m,n,k=map(int,sys.stdin.readline().split())
    graph=[[0]*(m) for _ in range(n)]

    for j in range(k):
        x,y=map(int,sys.stdin.readline().split())
        graph[y][x]=1

    #반복문을 돌면서 배추가 있는 경우에만 dfs로 확인
    for x in range(m):
        for y in range(n):
            if graph[y][x]==1:
                dfs(x,y)
                result+=1
    print(result)