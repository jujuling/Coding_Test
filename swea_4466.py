#import sys
#sys.stdin = open("input.txt", "r")

T=int(input())

for test_case in range(1,T+1):
    n,k=map(int,input().split())
    nlist=list(map(int,input().split()))
    nlist.sort(reverse=True)
    result=0
    for i in range(k):
        result+=nlist[i]
    print("#%d %d" %(test_case,result))