N,M =map(int, input().split())
l_s=[0 for i in range(N)]

for a in range(M):
    i,j,k=map(int, input().split())
    for b in range(i,j+1):
        l_s[b-1]=k

for i in range(N):
    print(l_s[i],end=" ")