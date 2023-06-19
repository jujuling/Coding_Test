import sys

m,n=map(int,sys.stdin.readline().split())
arr=[True]*(n+1)
arr[0]=False
arr[1]=False

for i in range(2,int(n**0.5)+1):

    if arr[i]:
        for j in range(i+i,n+1,i):
            arr[j]=False

for i in range(m,n+1):
    if arr[i]:
        print(i)