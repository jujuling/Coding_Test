list1=[]
for i in range(10):
    n=int(input())
    list1.append(n%42)

list2=set(list1)
list1=list(list2)
print(len(list1))
