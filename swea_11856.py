#import sys
#sys.stdin=open('sample_input.txt','r')

T=int(input())

for test_case in range(1,T+1):
    flag=0
    s=list(input())
    for i in s:
        if s.count(i)!=2:
            flag=1
            break
    if flag==0:
        print("#%d Yes" % (test_case))
    else:
        print("#%d No" %(test_case))