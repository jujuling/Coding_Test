import sys

n=int(sys.stdin.readline())

for i in range(1,n):
    print('*'*i,end='')
    print(' '*(n-i)*2,end='')
    print('*'*i)
print('*'*2*n)
for i in range(n-1,0,-1):
    print('*'*i,end='')
    print(' '*(n-i)*2,end='')
    print('*'*i)