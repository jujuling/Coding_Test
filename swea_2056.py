T=int(input())

for test_case in range(1,T+1):

    n=input()
    date=int(n[-2:])
    mon=int(n[-4:-2])
    year=int(n[:4])

    if mon>=1 and mon<=12:
        if mon%2!=0:
            if date>=1 and date<=31:
                print("#%d %04d/%02d/%02d" %(test_case,year,mon,date))
            else:
                print("#%d -1" % test_case)
        else: # 달이 짝수일 때,
            if mon==2:
                if date>=1 and date<=28:
                    print("#%d %04d/%02d/%02d" % (test_case, year, mon, date))
                else:
                    print("#%d -1" % test_case)
            else:
                if date>=1 and date<=30:
                    print("#%d %04d/%02d/%02d" % (test_case, year, mon, date))
                else:
                    print("#%d -1" % test_case)
    else:
        print("#%d -1" % test_case)