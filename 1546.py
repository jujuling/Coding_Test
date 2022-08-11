N=int(input())
a=list(map(int,input().split()))
M=max(a)
avg=0
for i in range(N):
    a[i]=a[i]/M*100
    avg+=a[i]

print(avg/N)
