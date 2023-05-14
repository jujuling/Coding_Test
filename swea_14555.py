#import sys
#sys.stdin = open("sample_input (2).txt")

T=int(input())

for test_case in range(1,T+1):
    s=input()
    result=0
    for i in range(len(s)-1):
        if s[i]=='(' and s[i+1]=='|' or s[i]=='|' and s[i+1]==')' or s[i]=='(' and s[i+1]==')':
            result+=1
    print("#%d %d" %(test_case,result))