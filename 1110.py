import sys

n=int(sys.stdin.readline())
flag=0

if n < 10:
    nn = '0' + str(n)
else:
    nn=str(n)
while True:
    hap=int(nn[0])+int(nn[1])
    hap=str(hap)
    w=nn[-1]+str(hap[-1])
    flag+=1
    if n==int(w) :
        break
    else:
        nn=w

print(flag)