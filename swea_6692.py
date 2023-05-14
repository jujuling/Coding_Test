#import sys
#sys.stdin = open("s_input.txt", "r")

T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    hap=0
    for i in range(n):
        p,x=input().split()
        hap+=float(p)*int(x)
    print("#%d %.6f" %(test_case,hap))