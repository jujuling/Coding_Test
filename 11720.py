N=int(input())
a=input()

total=0
a=int(a)
while a!=0:
    total = total+ a%10
    a=a//10

print(total)