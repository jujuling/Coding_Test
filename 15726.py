import sys

a,b,c=map(int,sys.stdin.readline().split())

num1=a*b/c
num2=a/b*c
print(int(max(num1,num2)))