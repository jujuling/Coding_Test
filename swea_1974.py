#import sys
#sys.stdin=open('input.txt','r')

T=int(input())

for test_case in range(1,T+1):
    s=[list(map(int,input().split())) for _ in range(9)]
    row=1 #행, 가로줄
    col=1 #열, 세로줄
    sq=1 # 3*3 박스
    #행 검사
    for i in range(9):
        a=[1,2,3,4,5,6,7,8,9]
        for j in range(9):
            if s[i][j] in a:
                a.remove(s[i][j])
            else:
                row=0
                break
    # 열 검사
    for i in range(9):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if s[j][i] in a:
                a.remove(s[j][i])
            else:
                col = 0
                break
    # 3*3 박스 검사
    for i in range(3):
        for j in range(3):
            a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for k in range(3):
                for l in range(3):
                    if s[3*i+k][3*j+l] in a:
                        a.remove(s[3*i+k][3*j+l])
                    else:
                        sq = 0
                        break

    if row==1 and col==1 and sq==1 :
        print("#%d %d" %(test_case,1))
    else:
        print("#%d %d" %(test_case,0))