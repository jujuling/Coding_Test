t=int(input())
a,b,c=0,0,0
flag=0
while 1 :
    if t>=300:
        a += 1
        t -= 300
        if t==0:
            flag=1
            break
        continue
    elif t>=60:
        b+=1
        t-=60
        if t==0:
            flag=1
            break
        continue
    elif t>=10:
        if t%10==0:
            c=t//10
            flag=1
            break
        else:
            break
    break

if flag==1:
    print(a,b,c)
else :
    print(-1)