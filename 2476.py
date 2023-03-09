n=int(input())
total=0
result=0
for _ in range(n):
    a,b,c=map(int,input().split())
    maxn=max(a,b,c)
    if a==b and b==c:
        same=10000+a*1000
        if result < same:
            result = same
    elif a!=b and a!=c and b!=c :
        differ=maxn*100
        if result < differ:
            result = differ
    else:
        if a==b and b!=c:
            two=1000+a*100
        elif a!=b and b==c :
            two=1000+b*100
        elif a==c and a!=b:
            two=1000+a*100
        if result<two:
            result=two
print(result)