import sys

result=0
while True:
    n=int(sys.stdin.readline())
    if n==-1:
        break
    result+=n
print(result)