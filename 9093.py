import sys

t=int(sys.stdin.readline())
for i in range(t):
    w=list(sys.stdin.readline().split())
    for j in w:
        print(j[::-1],end=' ')
    print()