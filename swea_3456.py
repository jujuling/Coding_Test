T=int(input())

for test_case in range(1,T+1):
    a,b,c=map(int,input().split())
    if a==b==c:
        print("#%d %d" %(test_case,a))
    elif a==b and b!=c:
        print("#%d %d" %(test_case,c))
    elif a!=b and b==c:
        print("#%d %d" % (test_case, a))
    elif a==c and b!=c:
        print("#%d %d" % (test_case, b))