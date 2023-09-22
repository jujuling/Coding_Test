import sys

n=int(sys.stdin.readline())
result=0
for i in range(n):
    schn,apn=map(int,sys.stdin.readline().split())
    result+=apn%schn
print(result)