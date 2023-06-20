import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
result=[0]*10
n = a*b*c

while n!=0:
    tmp=n%10
    result[tmp]+=1
    n//=10
for i in result:
    print(i)