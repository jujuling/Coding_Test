import sys
while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    origin=[]
    l=[]
    m=[]
    for i in range(n):
        tmp=sys.stdin.readline().strip()
        origin.append(tmp)
        tmp=tmp.lower()
        l.append(tmp)
        m.append(tmp)
    l.sort()
    idx=m.index(l[0])
    print(origin[idx])