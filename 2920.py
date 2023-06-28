import sys

l=list(map(int,sys.stdin.readline().split()))
num=list(range(1,9))
num2=list(range(8,0,-1))

if l==num:
    print("ascending")
elif l == num2:
    print("descending")
else:
    print("mixed")