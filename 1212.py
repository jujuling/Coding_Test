import sys

n=sys.stdin.readline().strip()
sn=int(n,8)
result=format(sn,'b')
print(result)