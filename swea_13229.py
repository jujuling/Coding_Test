T=int(input())
week={'MON':6, 'TUE':5, 'WED':4,'THU':3,'FRI':2, 'SAT':1,'SUN':0}
for test_case in range(1,T+1):
    s=input()
    for i,j in week.items():
        if s==i:
            if j==0:
                print("#%d %d" %(test_case,7))
            else:
                print("#%d %d" % (test_case, j))
