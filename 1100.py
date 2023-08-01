import sys

l=[]
for i in range(8):
    tmp=list(sys.stdin.readline().strip())
    l.append(tmp)
result=0
for i in range(8):
    if i%2!=0:
        for j in range(8):
            if j%2!=0 and l[i][j]=='F':
                result+=1
    else:
        for k in range(8):
            if k%2==0 and l[i][k]=='F':
                result+=1
print(result)