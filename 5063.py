n=int(input())

for _ in range(n):
    r,e,c=map(int,input().split())
    if e<r+c:
        print("do not advertise")
    elif e>r+c:
        print("advertise")
    else:
        print("does not matter")