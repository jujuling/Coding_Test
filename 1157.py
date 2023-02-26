S=input().upper()
a=list(set(S))
b=[]
for i in range(len(a)):
    b.append(S.count(a[i]))

if b.count((max(b)))>1:
    print("?")
else:
    idx=b.index(max(b))
    print(a[idx])