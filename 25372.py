import sys

n=int(sys.stdin.readline())

for i in range(n):
    l=list(map(str,sys.stdin.readline().strip()))
    if len(l)>=6 and len(l)<=9:
        print("yes")
    else:
        print("no")