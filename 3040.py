from itertools import combinations
import sys

l=[]
for i in range(9):
    l.append(int(sys.stdin.readline()))

d=list(combinations(l,7))

for i in d:
    if sum(i)==100:
        for j in i:
            print(j)
        break