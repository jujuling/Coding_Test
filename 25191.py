n=int(input())
a,b=map(int,input().split())
result=a//2+b

if result>n:
    print(n)
else:
    print(result)