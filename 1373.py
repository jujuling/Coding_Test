import sys
n=list(map(int,sys.stdin.readline().strip()))
leng=len(n)//3
cutlist=[] #3개씩 자른 숫자를 저장할 리스트
tmp=[] #임시 리스트
flag=0 #3개씩 자르기 위한 index
n.reverse() #맨 뒷자리부터 2^0이기 때문에 편하게 계산하기 위해서 거꾸로 정렬했다.

for i in range(leng*3): #예제가 8자리이면 3의 배수길이만큼만 출력하기위해 길이를 임의로 설정(6개까지만 가능하도록)
    if flag==2: #숫자가 3개인 걸 확인했다면
        tmp.append(n[i])
        tmp.reverse() #원래 대로 저장하기 위해 다시 거꾸로 정렬하고
        cutlist.append(tmp)  #임시리스트에 저장된 값을 cutlist에 저장
        tmp=[] #임시리스트 비우기
        flag=0 #index값도 초기화
    else: #만약 숫자가 3개가 안되었으면, 그냥 임시리스트에 추가함
        tmp.append(n[i])
        flag+=1

#나머지 저장못한 값들을 추가해주는 과정
if len(n[leng*3:])!=0: #만약 남은 n리스트값이 있다면 진행하고 아니라면 pass
    tmp=n[leng*3:]
    if len(tmp)==1: #tmp 원소가 1개라면 0을 두 번 추가
        tmp.append(0)
        tmp.append(0)
    elif len(tmp)==2: #tmp 원소가 2개라면 0 한 번 추가
        tmp.append(0)
    tmp.reverse()
    cutlist.append(tmp)
cutlist.reverse()

result=[] #result는 최종 8진수로 변환한 값을 저장할 리스트
for i in range(len(cutlist)):
    tmp=0
    for j in range(3):
        tmp+=cutlist[i][j]* 2**(2-j)
    result.append(tmp)
#출력하기
for i in result:
    print(i,end='')