#import sys
#sys.stdin=open('input.txt','r')

T=int(input())
for t in range(1,T+1):
    n=int(input())
    dis=0
    speed=0

    for i in range(n):
        c=list(map(int,input().split()))
        #0일 경우에는 속도를 유지한다.
        if c[0]==0:
            dis += speed
        #가속
        elif c[0]==1:
            speed+=c[1]
            dis+=speed
        #감속
        elif c[0]==2:
            if speed<c[1]:
                speed=0
            else:
                speed-=c[1]
                dis+=speed
    print("#%d %d" %(t,dis))