T=int(input())

for test_case in range(1,T+1):
    l,u,x=map(int,input().split())
    if x>u:
        print("#%d %d" %(test_case,-1))
    elif x<l:
        print("#%d %d" %(test_case,l-x))
    elif x>=l:
        print("#%d %d" % (test_case, 0))