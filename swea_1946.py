#import sys
#sys.stdin=open('input.txt','r')

T=int(input())
for t in range(1,T+1):
    n=int(input())
    #문자를 저장할 문자열 arr
    arr=''
    #c와 k를 입력받으면서 바로 문자열에 c*k만큼 저장한다.
    for i in range(n):
        c,k=input().split()
        arr+=c*int(k)

    print("#%d" %t)
    flag=1
    #원본문서의 너비가 10이므로,
    #for문을 돌면서 10이 되면 줄을 바꾸고 출력
    for i in range(len(arr)):
        if flag==10:
            print(arr[i])
            flag=1
        else:
            print(arr[i],end='')
            flag+=1
    print()