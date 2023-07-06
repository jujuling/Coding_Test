import sys

n=list(sys.stdin.readline().strip())
idx={'000':0, '001':1, '010':2, '011':3, '100':4, '101':5,'110':6,'111':7}

while(len(n)%3!=0):
    tmp=['0']
    n=tmp+n

nl=[]
tmp = []
flag=0
for i in range(len(n)):
    tmp.append(n[i])
    if flag==2:
        newn=''.join(tmp)
        nl.append(newn)
        tmp.clear()
        flag=0
    else:
        flag+=1

for i in nl:
    if i in idx.keys():
        print(idx[i],end='')