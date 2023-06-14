import sys

n=int(sys.stdin.readline())
d=[]

for i in range(n):
    b=list(map(str,sys.stdin.readline().split()))

    if b[0]=='push_front':
        a=[int(b[1])]
        d=a+d
    elif b[0]=='push_back':
        d.append(int(b[1]))
    elif b[0]=='pop_front':
        if len(d)==0:
            print(-1)
        else:
            print(d[0])
            d.remove(d[0])
    elif b[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif b[0]=='size':
        print(len(d))
    elif b[0]=='empty':
        if len(d)==0:
            print(1)
        else:
            print(0)
    elif b[0]=='front':
        if len(d)==0:
            print(-1)
        else:
            print(d[0])
    else: #back
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])