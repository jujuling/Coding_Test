import sys

n=int(sys.stdin.readline())
l=[]
for i in range(n):
    s=sys.stdin.readline().strip()
    l.append(s)

dcnt=0
pcnt=0
for i in l:
    if abs(dcnt-pcnt)>1:
        break
    if i=='D':
        dcnt+=1
    else:
        pcnt+=1

print("%d:%d" %(dcnt,pcnt))