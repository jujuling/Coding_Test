import sys

n=int(sys.stdin.readline())
l=list()
for i in range(n):
    l.append(int(sys.stdin.readline()))
if len(l)==l.count(1):
    print(1)
else:
    print(sum(l)-(n-1))