import sys

n=int(sys.stdin.readline())
nl=list(map(int,sys.stdin.readline().split()))
m=0
y=0

for i in range(n):
    y+=(nl[i]//30)*10+10
    m+=(nl[i]//60)*15+15
if y==m:
    print("Y M %d"%y)
elif y>m:
    print("M %d"%m)
else:
    print("Y %d"%y)