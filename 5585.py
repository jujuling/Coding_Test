import sys

n=int(sys.stdin.readline())

c=1000-n
result=0

while c!=0:
    if c>=500:
        c-=500
        result+=1
    elif c>=100:
        c-=100
        result+=1
    elif c>=50:
        c-=50
        result+=1
    elif c>=10:
        c-=10
        result+=1
    elif c>=5:
        c-=5
        result+=1
    else:
        c-=1
        result+=1
print(result)