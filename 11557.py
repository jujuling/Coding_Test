t=int(input())
for i in range(t):
    n=int(input())
    max=0
    for j in range(n):
        a,b=(map(str,input().split()))
        if max<int(b):
            max=int(b)
            name=a
    print(name)