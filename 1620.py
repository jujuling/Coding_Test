import sys

n,m=map(int,sys.stdin.readline().split())
l=dict()
for i in range(n):
    tmp=sys.stdin.readline().strip()
    l[i]=tmp

reverse_l =dict(map(reversed,l.items()))

for i in range(m):
    tmp=sys.stdin.readline().strip()
    if tmp.isdigit() :
        print(l[int(tmp)-1])
    else:
        print(reverse_l[tmp]+1)