#import sys
#sys.stdin =open('input.txt','r')

T=int(input())

for test_case in range(1,T+1):
    s=list(input())
    leng=[]
    for i in range(len(s)):
        leng.append(s.count(s[i]))
    result=[]
    for i in range(len(s)):
        if leng[i]%2!=0:
            if s[i] not in result:
                result.append(s[i])
    result.sort()
    result=''.join((result))
    if result=='':
        print("#%d Good" %(test_case))
    else:
        print("#%d %s" %(test_case,result))