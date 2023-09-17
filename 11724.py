import sys

def bfs(v):
    queue=[v]
    visited[v]=1
    while queue:
        v=queue.pop(0)
        for i in range(1,n+1):
            if graph[v][i]==1 and visited[i]==0:
                queue.append(i)
                visited[i]=1

n,m=map(int,sys.stdin.readline().split())
graph=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u][v]=1
    graph[v][u]=1

visited=[0]*(n+1)

result=0
for i in range(1,n+1):
    if visited[i]==0:
        bfs(i)
        result+=1
print(result)