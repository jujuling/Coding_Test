import sys

t=int(sys.stdin.readline())

for i in range(t):
    tmp=sys.stdin.readline()
    n=int(sys.stdin.readline())
    l=[]
    for j in range(n):
        l.append(int(sys.stdin.readline()))
    if sum(l)%n==0:
        print("YES")
    else:
        print("NO")