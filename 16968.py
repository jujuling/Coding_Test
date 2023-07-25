import sys

m=list(map(str,sys.stdin.readline().strip()))
result=1
for i in range(len(m)):
    if m[i]=='c':
        if i!=0 and m[i-1]=='c':
            result*=25
        else:
            result*=26
    else:
        if i!=0 and m[i-1]=='d':
            result*=9
        else:
            result*=10
print(result)