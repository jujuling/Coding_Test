N,M =map(int, input().split())
l_s=[0 for i in range(N)]

for i in range(N):
    l_s[i]=l_s[i]+i+1


for a in range(M):
    i,j=map(int, input().split())
    tmp=l_s[i-1]
    l_s[i-1]=l_s[j-1]
    l_s[j-1]=tmp

for i in range(N):
    print(l_s[i],end=" ")