import sys

n,l=map(int,sys.stdin.readline().split())
fruit=list(map(int,sys.stdin.readline().split()))
fruit.sort()
for i in range(n):
    if fruit[i]<=l:
        l+=1
print(l)