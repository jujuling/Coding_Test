import sys

def gop(a,b):
    return (a+b)*(a-b)

a,b=map(int,sys.stdin.readline().split())
print(gop(a,b))