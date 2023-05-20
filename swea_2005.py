T=int(input())
for t in range(1,T+1):
    n=int(input())
    #n==1 , n==2 일때는 고정
    l=[[1],[1,1]]

    #n==3 일때부터 한줄씩 추가
    for i in range(2,n):
        #첫 번째 숫자는 무조건 1이 와야함
        tmp = [1]
        #반복문을 돌면서 가로 길이에 들어갈 숫자들을 정하기
        for j in range(1,i):
            #윗 줄 왼쪽,오른쪽을 더해서 값으로 가지기
            tmp.append(l[i-1][j-1]+l[i-1][j])
        #마지막은 1로 닫아야함
        tmp.append(1)
        #추가된 줄을 최종 l배열에 저장함
        l.append(tmp)

    print("#%d"%t)
    for i in range(n):
        for j in l[i]:
            print(j,end=' ')
        print()