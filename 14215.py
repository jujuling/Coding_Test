import sys

a,b,c=map(int,sys.stdin.readline().split())

big=max(a,b,c)
na=0 #나머지
if big==a:
    na=b+c
elif big==b:
    na=a+c
else:
    na=a+b

if na>big:
    print(na+big)
else:
    print(na+na-1)