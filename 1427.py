import sys

n=int(sys.stdin.readline())
l=[]
while n!=0:
    l.append(n%10)
    n//=10

l.sort(reverse=True)
for i in l:
    print(i,end='')