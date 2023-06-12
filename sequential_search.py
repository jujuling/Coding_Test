def sq_search(n,target,arr):
    for i in range(n):
        if arr[i]==target:
            return i+1

arr = ['apple','banana','grape','peach','lemon']
n= len(arr)
target = arr[2]

print("{}번째에서 데이터 탐색 종료.".format(sq_search(n,target,arr)))