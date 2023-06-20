import sys

n,m=map(int,sys.stdin.readline().split())
card=list(map(int,sys.stdin.readline().split()))
max_n=0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k]<=m and max_n<card[i]+card[j]+card[k]:
                max_n=card[i]+card[j]+card[k]
print(max_n)