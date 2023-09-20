import sys

n=int(sys.stdin.readline())
l=[]
for i in range(n):
    l.append(sys.stdin.readline().strip())
l=list(set(l))
l.sort(key=lambda x:(len(x),x))

for i in l:
    print(i)