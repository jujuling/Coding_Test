import sys
from itertools import combinations

l=[]
for i in range(9):
    l.append(int(sys.stdin.readline()))

cl=list(combinations(l,7))

for i in cl:
    if sum(i)==100:
        i=sorted(i)
        for j in i:
            print(j)
        break