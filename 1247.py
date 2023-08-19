import sys

for i in range(3):
    n=int(sys.stdin.readline())
    l=[]
    for j in range(n):
        l.append(int(sys.stdin.readline()))
    if sum(l)==0:
        print(0)
    elif sum(l)>0:
        print('+')
    else:
        print('-')