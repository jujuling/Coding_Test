import sys

#dfs 함수
def dfs(v):
    #v를 방문처리해서 True로 저장한다.
    visited[v]=True
    #방문처리한 노드는 출력
    print(v,end=' ')
    #반복문을 돌면서 1번 노드와 인접한 노드들이 있는지 확인한다.
    for i in range(1,n+1):
        #만약 인접한 노드가 있고, 아직 방문하지 않았다면 (false는 방문처리 아직 안됨)
        if graph[v][i]==True and visited[i]==False:
            dfs(i) #dfs를 수행한다.

#bfs 함수
def bfs(v):
    queue=[v]
    visited[v]=True #방문처리
    while queue:
        v=queue.pop(0) #해당방문한 노드를 제거하고 출력
        print(v,end=' ')
        #반복문을 돌면서 인접한 노드가있고, 아직 방문하지 않았다면
        for i in range(1,n+1):
            if graph[v][i]==True and visited[i]==False:
                queue.append(i) #queue에 원소들을 전부 삽입하고
                visited[i]=True #방문처리해준다.

n,m,v=map(int,sys.stdin.readline().split())

#그래프 행렬만들기 (False로 초기화)
graph=[[False] *(n+1) for _ in range(n+1)]
for i in range(m):
    #노드들을 입력받아 해당 노드들만 True로 바꿔줌
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=True
    graph[b][a]=True

visited=[False]*(n+1)
dfs(v)
visited=[False]*(n+1)
print()
#dfs를 수행하면서 visited가 바뀌었을 것이므로 visited를 다시 초기화
bfs(v)