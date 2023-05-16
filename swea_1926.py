n=int(input())
for i in range(1,n+1):
    num=0
    zn=i
    while i!=0:
        tmp=i%10
        if tmp==3 or tmp==6 or tmp==9:
            num+=1
        i//=10
    l = '-'
    l *= num
    if num==0:
        print(zn,end=' ')
    else:
        print(l,end=' ')