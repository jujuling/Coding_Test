#import sys
#sys.stdin=open('input.txt','r')

T=int(input())
for t in range(1,T+1):
    #테스트 케이스 입력
    tc=int(input())
    #리스트로 숫자 받기
    l=list(map(int,input().split()))
    #점수는 0~100까지 총 101개이므로 빈도수를 받기위한 배열cnt만들기
    cnt=[0]*101

    #숫자가 저장된 l을 돌면서 숫자가 나오면 갯수를 cnt에 저장
    for i in l:
        cnt[i]+=1
    #a배열을 새로 만든 이유는 최빈수가 여러 개일 때, 가장 큰 점수를 출력하기 위해서!
    a=[]
    #일단 갯수를 저장해 놓은 cnt배열에서 최빈수를 찾는다.
    findn=max(cnt)

    #cnt 배열을 끝에서 부터 반복문을 돌려서, findn과 같은 수의 index만 a에 저장한다. 
    for i in range(len(cnt)-1,0,-1):
        print(i)
        if findn==cnt[i]:
            a.append(i)
    #a값중 a[0]이 최빈수 중 제일 큰 점수        
    print("#%d %d"%(tc,a[0]))
