#import sys
#sys.stdin=open('sample_input.txt','r')

T=int(input())

for test_case in range(1,T+1):
    s=input()
    xnum=0
    onum=0
    for i in s:
        if i =='x':
            xnum+=1
        else:
            onum +=1

    if onum>=8 or xnum<8:
        print("#%d YES" %test_case)
    else:
        print("#%d NO" %(test_case))