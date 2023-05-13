#import sys
#sys.stdin = open("input.txt", "r")

T=int(input())

for test_case in range(1,T+1):
    n,k=map(int,input().split())
    result=0
    flag = 0
    nlist=[]
    for i in range(n):
        nlist.append(list(map(int,input().split())))


    #가로줄 확인
    for i in range(n):
        for j in range(n):
            #반복문을 돌면서 만약 1일 경우 flag 갯수를 증가시켜서 나중에
            #k값과 같은지 확인할 것
            if nlist[i][j] == 1:
                flag+=1
            #만약 검은부분 0을 만나거나 반복문이 끝나게 되면
            if nlist[i][j]==0 or j==n-1:
                #flag값이 k랑 같은지 확인해서 맞을 경우 result 증가
                if flag==k:
                    result+=1
                #조건문이 맞다면 검은부분을 만난 후, 다시 k자리가 마련될 수 있으므로,
                #flag 초기화해줌
                #만약 끝까지 탐색했을 경우(j==n-1)더라도 flag 초기화가 필요
                flag=0
    #세로줄 확인
    for i in range(n):
        for j in range(n):
            #반복문을 돌면서 만약 1일 경우 flag 갯수를 증가시켜서 나중에
            #k값과 같은지 확인할 것
            if nlist[j][i]==1:
                flag+=1
            # 만약 검은부분 0을 만나거나 반복문이 끝나게 되면
            if nlist[j][i]==0 or j==n-1:
                #flag값이 k랑 같은지 확인해서 맞을 경우 result 증가
                if flag == k:
                    result += 1
                # 조건문이 맞다면 검은부분을 만난 후, 다시 k자리가 마련될 수 있으므로,
                # flag 초기화해줌
                # 만약 끝까지 탐색했을 경우(j==n-1)더라도 flag 초기화가 필요
                flag=0
    print("#%d %d" %(test_case,result))