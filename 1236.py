import sys

n,m=map(int,sys.stdin.readline().split())
l=[]
for i in range(n):
    l.append(list(sys.stdin.readline().strip()))

#X가 없는 행 개수 row
#X가 없는 열 개수 col
row,col=0,0

for i in range(n):
    if l[i].count('X')==0:
        row+=1
for i in range(m):
    cnt=0
    for j in range(n):
        if l[j][i]=='X':
            cnt+=1
    if cnt==0:
        col+=1

print(max(row,col))