import sys

n=int(sys.stdin.readline())

for i in range(n):
    print(" "*(n-i-1),end='')
    print("*"*(i+1))
for i in range(n-1):
    print(" "*(i+1),end='')
    print("*"*(n-1-i))