import sys

l=[]
for i in range(5):
    tmp=list(map(int,sys.stdin.readline().split()))
    l.append(sum(tmp))
print(l.index(max(l))+1,max(l))