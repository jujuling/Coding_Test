T=int(input())

for test_case in range(1,T+1):
    n2=0
    n3=0
    n5=0
    n7=0
    n11=0
    n=int(input())
    while n%2==0:
        n2+=1
        n//=2
    while n%3==0:
        n3+=1
        n//=3
    while n%5==0:
        n5+=1
        n//=5
    while n%7==0:
        n7+=1
        n//=7
    while n%11==0:
        n11+=1
        n//=11

    print("#%d %d %d %d %d %d" %(test_case,n2,n3,n5,n7,n11))