N=int(input())
str=input()
a=list(str.split())
V=int(input())

num=0
for i in range(N):
    if int(a[i])==V:
        num = num + 1

print(num)
