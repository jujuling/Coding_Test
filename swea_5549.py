T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    if n%2==0:
        print("#%d %s" %(test_case,"Even"))
    else:
        print("#%d %s" % (test_case, "Odd"))