import sys

check=1
while True:
    l,p,v=map(int,sys.stdin.readline().split())
    if l==p==v==0:
        break
    result=v//p*l
    if v%p>l:
        result+=l
    else:
        result+=v%p
    print("Case %d: %d" %(check,result))
    check+=1