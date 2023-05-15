#import sys
#sys.stdin=open('input.txt','r')

T=int(input())

for test_case in range(1,T+1):
    a,b,c=map(int,input().split())
    result=c//(min(a,b))
    print("#%d %d" %(test_case,result))