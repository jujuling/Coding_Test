import sys

n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
b,c=map(int,sys.stdin.readline().split())

result=0
for i in range(len(l)):
    tmp=0
    if l[i]%b==0:
        if l[i]//b==1:
            result+=1
        else:
            result+=1
            tmp=l[i]-b
    else:
        if l[i] < b:
            result += 1
            continue
        result+=1
        tmp=l[i]-b
    if tmp!=0:
        result+=tmp//c
        if tmp%c!=0:
            result+=1
print(result)