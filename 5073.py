import sys

while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b==c==0 :
        break
    if max(a,b,c)>=((a+b+c)-max(a,b,c)):
        print("Invalid")
    else:
        if a==b==c :
            print("Equilateral")
        elif a!=b and b!=c and a!=c:
            print("Scalene")
        else:
            print("Isosceles")