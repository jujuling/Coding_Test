import sys

n=int(sys.stdin.readline())
l=[]
flag=[]
result=[]
for i in range(n):
    tmp=sys.stdin.readline().strip()
    l.append(tmp[0])
    if tmp[0] not in flag:
        flag.append(tmp[0])

for i in flag:
    if l.count(i)>4:
        result.append(i)
if len(result)==0:
    print("PREDAJA")
else:
    result.sort()
    for i in result:
        print(i,end='')