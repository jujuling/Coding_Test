import sys

n=int(sys.stdin.readline())
l=[]

for i in range(n):
    l.append(sys.stdin.readline().strip())

result=list(l[0])
for i in range(1,n):
    for j in range(len(l[i])):
        if l[i][j]!=result[j]:
            result[j]='?'
print(''.join(result))