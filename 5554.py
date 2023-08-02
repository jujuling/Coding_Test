import sys

result=0
for i in range(4):
    n=int(sys.stdin.readline())
    result+=n

print(result//60)
print(result%60)