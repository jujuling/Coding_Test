import sys
n=int(sys.stdin.readline())

l=[]
for i in range(n):
    l.append(list(map(int,sys.stdin.readline().split())))

result=0
for i in l:
    if i[0]==136:
        result+=1000
    elif i[0]==142:
        result+=5000
    elif i[0]==148:
        result+=10000
    else:
        result+=50000
print(result)