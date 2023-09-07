import sys

a,b=map(str,sys.stdin.readline().split())
la=list(a)
lb=list(b)
maxa=[]
mina=[]
maxb=[]
minb=[]

for i in range(len(la)):
    if la[i]=='5' or la[i]=='6':
        mina.append('5')
        maxa.append('6')
    else :
        mina.append(la[i])
        maxa.append(la[i])
for i in range(len(lb)):
    if lb[i]=='5' or lb[i]=='6':
        minb.append('5')
        maxb.append('6')
    else :
        minb.append(lb[i])
        maxb.append(lb[i])

maxa=''.join(maxa)
maxb=''.join(maxb)
mina=''.join(mina)
minb=''.join(minb)

print(int(mina)+int(minb),int(maxa)+int(maxb))