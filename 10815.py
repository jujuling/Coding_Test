import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))

a.sort()

def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

for i in range(m):
    if binary_search(a,b[i],0,n-1) is not None:
        print("1",end=' ')
    else:
        print("0",end=' ')