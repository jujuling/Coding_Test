import sys

l=[]
for i in range(10):
    l.append(int(sys.stdin.readline()))
l.sort()
m=[]
for i in range(10):
    m.append(l.count(l[i]))

print(sum(l)//10)
flag=m.index(max(m))
print(l[flag])