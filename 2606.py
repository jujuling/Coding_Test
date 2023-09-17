import sys

result=0
def dfs(v):
    #result를 전역변수로 사용함 (global 사용하여)
    global result
    visited[v]=1
    result += 1
    for i in range(1,n+1):
        if graph[v][i]==1 and visited[i]==0:
            dfs(i)

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=1
    graph[b][a]=1

visited=[0]*(n+1)
dfs(1)

print(result-1)