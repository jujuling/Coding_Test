#import sys
#sys.stdin = open("sample_input.txt", "r")

T=int(input())

for test_case in range(1,T+1):
    s=list(input())
    h=int(input())
    hlist=list(map(int,input().split()))
    for i in hlist:
        if i==0:
            s[0]='-'+s[0]
        for j in range(len(s)):
            if j==i-1:
                s[i-1]=s[i-1]+'-'
    s=''.join(s)
    print("#%d %s" %(test_case,s))