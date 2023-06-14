import sys
stack=[]

def push(x):
    stack.append(x)

def top(arr):
    leng=len(arr)
    return arr[leng-1]

n=int(sys.stdin.readline())

for i in range(n):
    b=list(map(str,sys.stdin.readline().split()))
    if b[0]=='push':
        push(int(b[1]))
    elif b[0]=='pop':
        if len(stack)==0:
            print(-1)
        else :
            tmp=stack.pop()
            print(tmp)
    elif b[0]=='size':
        print(len(stack))
    elif b[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif b[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(top(stack))