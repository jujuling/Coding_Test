import sys

n=int(sys.stdin.readline())
l=[]
for i in range(n):
    l.append(sys.stdin.readline().strip())

if l==sorted(l):
    print("INCREASING")
elif l==sorted(l,reverse=True):
    print("DECREASING")
else:
    print("NEITHER")