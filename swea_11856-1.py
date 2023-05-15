#import sys
#sys.stdin=open('sample_input.txt','r')

T=int(input())

for test_case in range(1,T+1):
    flag=0
    s=list(input())
    s.sort()
    if s[0]==s[1] and s[2]==s[3] and s[1]!=s[2]:
        print("#%d Yes" % (test_case))
    else:
        print("#%d No" %(test_case))
