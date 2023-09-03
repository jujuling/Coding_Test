import sys

dic={'A':10, 'B':11,'C':12,'D':13,'E':14,'F':15}
n=list(sys.stdin.readline().strip())
l=[]
for i in n :
    if i in dic:
        l.append(dic[i])
    else:
        l.append(int(i))
result=0
l.reverse()
for i in range(len(l)) :
    result+=l[i]*(16**i)
print(result)