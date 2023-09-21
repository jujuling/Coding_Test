import sys

n=int(sys.stdin.readline())
nl=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
ml=list(map(int,sys.stdin.readline().split()))

cnt=dict()
#구하고 싶은 숫자카드들을 cnt 딕셔너리의 key로 설정
#구하고 싶은 숫자카드의 개수는 아직 모르니까 0개로 설정
for i in range(m):
    cnt[ml[i]]=0

#저장된 모든 숫자들을 보면서
for i in range(n):
    #만약 cnt 딕셔너리에 값이 있다면 숫자의 갯수를 증가시킨다.
    #딕셔너리에 없는 값이라면 굳이 셀 필요없으므로 조건을 주지 않았다.
    if nl[i] in cnt:
        cnt[nl[i]]+=1

#m만큼 반복문을 돌면서 ml 리스트에 있는 숫자의 갯수를 각각 출력해준다. 
for i in range(m):
    print(cnt[ml[i]],end=' ')