import sys

t=int(sys.stdin.readline())

for i in range(t):
    w=int(sys.stdin.readline())
    t=[1]
    for j in range(2,w+2):
        t.append(t[j-2]+j)
    sum=0
    for k in range(1,w+1):
        sum+=k*t[k]
    print(sum)