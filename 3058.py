import sys

t=int(sys.stdin.readline())

for i in range(t):
    l=list(map(int,sys.stdin.readline().split()))
    select=[]
    for j in l:
        if j%2==0:
            select.append(j)
    print(sum(select),min(select))