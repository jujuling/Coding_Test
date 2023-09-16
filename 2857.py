import sys

l=[]
for i in range(5):
    l.append(sys.stdin.readline().strip())

flag=[]
for i in l:
    if "FBI" in i:
        flag.append(l.index(i)+1)
if len(flag)==0:
    print("HE GOT AWAY!")
else:
    for i in flag:
        print(i,end=' ')