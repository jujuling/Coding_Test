import sys
from collections import deque

def bfs(i,j,rain):
    queue=deque()
    visited[i][j]=1
    queue.append((i,j))
    #상하좌우 계산
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #범위안에 있고
            if nx in range(n) and ny in range(n):
                if not visited[nx][ny]:#방문하지 않은 지역이며
                    if graph[nx][ny]>rain : #강수량보다 높은 지역이면
                        visited[nx][ny]=1 #방문처리
                        queue.append((nx,ny))

n=int(sys.stdin.readline())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

#최대 높이값을 찾는다.
high=0
for i in range(n):
    for j in range(n):
        if graph[i][j]>high:
            high=graph[i][j]

result=0
#높이의 최댓값까지 반복함
for k in range(high):
    visited=[[0]*n for _ in range(n)]
    numb=0

    for i in range(n):
        for j in range(n): #반복문 돌면서 만약 방문하지 않은 지역이면 bfs실행
            if graph[i][j]>k and visited[i][j]==0:
                bfs(i,j,k)
                numb+=1 #안전영역이 추가됨
        if numb>result: #안전영역 최댓값 저장하는 과정
            result=numb
print(result)