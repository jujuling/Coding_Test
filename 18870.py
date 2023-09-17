import sys

n=int(sys.stdin.readline())
x=list(map(int,sys.stdin.readline().split()))

#python 얕은 복사(shallow copy)
#dx=x[:] 로도 가능
dx=set(x.copy())
dx=list(dx)
dx.sort()

nd=dict()
for i in range(len(dx)):
    nd[dx[i]]=i

for i in x:
    print(nd[i],end=' ')