t=int(input())

for i in range(t):
    ycnt,kcnt = 0,0
    for j in range(9):
        y,k=map(int, input().split())
        ycnt+=y
        kcnt+=k
    if ycnt>kcnt:
        print("Yonsei")
    elif ycnt<kcnt:
        print("Korea")
    else:
        print("Draw")