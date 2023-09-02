import sys

l=list()
for i in range(10):
    l.append(int(sys.stdin.readline()))
h=sum(l)-l[0]
print(l[0]-h)