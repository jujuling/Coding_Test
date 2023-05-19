T=int(input())

for t in range(1,T+1):
    l=list(map(int,input().split()))
    l.sort()
    total=0
    for i in range(1,9):
        total+=l[i]
    print("#%d %d"%(t,round(total/8)))