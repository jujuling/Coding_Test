import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    tmp=list(map(int,sys.stdin.readline().split()))
    arr.append(tmp)

y=sorted(arr,key=lambda x:(x[1],x[0]))
for i in range(n):
    print(y[i][0],y[i][1])