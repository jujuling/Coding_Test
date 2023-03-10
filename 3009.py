lx=list()
ly=list()
for _ in range(3):
    x,y=map(int, input().split())
    if lx.count(x)==0:
        lx.append(x)
    else :
        lx.remove(x)
    if ly.count(y)==0:
        ly.append(y)
    else :
        ly.remove(y)

print(lx[0],ly[0])