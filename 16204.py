import sys

n,m,k=map(int,sys.stdin.readline().split())

print(min(m, k) + n - max(m, k)) #둘 중 작은 것 + 둘 중 큰 것