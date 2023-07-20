import sys
n=[]
for i in range(7):
    tmp=int(sys.stdin.readline())
    if tmp%2!=0:
        n.append(tmp)
if len(n)==0:
    print(-1)
else:
    print(sum(n))
    print(min(n))