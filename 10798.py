import sys

l=[]
maxlen=0
for i in range(5):
    tmp=list(sys.stdin.readline().strip())
    if len(tmp)>maxlen:
        maxlen=len(tmp)
    l.append(tmp)

for i in range(5):
    if len(l[i])<maxlen:
        for j in range(maxlen-len(l[i])):
            l[i].append(' ')
for i in range(maxlen):
    for j in range(5):
        if l[j][i]!=' ':
            print(l[j][i],end='')