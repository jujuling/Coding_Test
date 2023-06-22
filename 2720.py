import sys
t=int(sys.stdin.readline())
for i in range(t):
    c=int(sys.stdin.readline())
    list=[0]*4
    check=0
    while c!=0:
        if check==0:
            list[0]=c//25
            c%=25
            check=1

        elif check==1:
            list[1]=c//10
            c%=10
            check=2
        elif check==2:
            list[2]=c//5
            c%=5
            check=3
        else:
            list[3]=c
            c%=1
    for j in list:
        print(j,end=' ')
    print()