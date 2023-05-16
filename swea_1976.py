#import sys
#sys.stdin = open('input.txt','r')

T=int(input())

for test_case in range(1,T+1):
    h1,m1,h2,m2 = map(int,input().split())
    t_h=h1+h2
    t_m=m1+m2
    if t_m>=60:
        t_m-=60
        t_h+=1
    if t_h>12:
        t_h-=12

    print("#%d %d %d" %(test_case,t_h,t_m))