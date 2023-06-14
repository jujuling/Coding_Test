import sys

n=int(sys.stdin.readline())
q=[]

for i in range(n):
    b=list(map(str,sys.stdin.readline().split()))

    if b[0]=='push':
        q.append(int(b[1]))
    elif b[0]=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
            q.remove(q[0])
    elif b[0]=='size':
        print(len(q))
    elif b[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif b[0]=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    else: #back
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])