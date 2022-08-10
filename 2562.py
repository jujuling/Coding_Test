list1=[]
for i in range(9):
    n=int(input())
    list1.append(n)
result=max(list1)
print(result)
print(list1.index(result)+1)
