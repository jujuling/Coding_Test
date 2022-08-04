a,b,c = map(int,input().split())

if a==b and b==c:
    result = 10000+a*1000
elif (a==b and b!=c) or (a==c and a!=b)  :
    result = 1000+a*100
elif (b==c and a!=b):
    result = 1000+b*100
else :
    result = max(a,b,c)
    result *=100

print(result)
