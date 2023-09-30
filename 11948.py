import sys

l=[]
m=[]
for i in range(4):
    l.append(int(sys.stdin.readline()))
for i in range(2):
    m.append(int(sys.stdin.readline()))

l.sort()
m.sort()
print(sum(l[1:])+m[1])