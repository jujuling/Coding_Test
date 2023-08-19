import sys

n=int(sys.stdin.readline())
q=list(range(1,n+1))
d_n=[]

while len(q)!=1:
    d_n.append(q.pop(0))
    q.append(q[0])
    q.pop(0)

d_n=d_n+q
for i in range(len(d_n)):
    print(d_n[i], end=' ')