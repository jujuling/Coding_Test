import sys

ans=list(sys.stdin.readline().strip())
st=list(sys.stdin.readline().strip())

if len(ans)>=len(st):
    print("go")
else:
    print("no")