def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else: #arr[mid]<target
            start=mid+1
    return None

arr =[0,2,4,6,8,10,12,14,16,18]
n=len(arr)
target=4
result=binary_search(arr,target,0,n-1)
print("{}번째에서 타겟 확인".format(result+1))