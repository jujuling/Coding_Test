def binary_search(arr,target,start,end):
    if start>end:
        return None

    mid=(start+end)//2

    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,target,start,mid-1)
    else: #arr[mid]<target
        return binary_search(arr,target,mid+1,end)

arr =[0,2,4,6,8,10,12,14,16,18]
n=len(arr)
target=4
result=binary_search(arr,target,0,n-1)
print("{}번째에서 타겟 확인".format(result+1))