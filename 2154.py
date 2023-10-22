import sys

n=sys.stdin.readline().strip()
l=[]

for i in range(1,100001):
    l.append(str(i))
result=''.join(l)

if n in result:
    print(result.index(n)+1)