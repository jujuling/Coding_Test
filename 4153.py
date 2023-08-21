import sys

while True:
    result=0
    a,b,c=map(int,sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break
    maxnz=max(a,b,c) **2
    if max(a,b,c)==a:
        result=b**2 + c**2
    elif max(a,b,c)==b:
        result = a ** 2 + c ** 2
    else:
        result = a ** 2 + b ** 2

    if maxnz == result:
        print("right")
    else:
        print("wrong")