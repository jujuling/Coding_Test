t=int(input())
for _ in range(t):
    a=list(map(str,input().split()))
    total=float(a[0])
    for i in a:
        if i=='@':
            total*=3
        elif i=='%':
            total+=5
        elif i=='#':
            total-=7
    print("%.2f" %total)