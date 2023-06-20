import sys
copy=[]
l=[]
#8개의 점수를 리스트에 저장
#l은 높은 점수 5개를 구하기 위해 저장
#copy는 인덱스를 구하기 위해 저장
for i in range(8):
    tmp=int(sys.stdin.readline())
    l.append(tmp)
    copy.append(tmp)
#l을 내림차순으로 정렬
l.sort(reverse=True)
total=0

#반복문을 돌면서 높은 점수 5개를 저장하는 동시에
#해당 수의 인덱스를 찾아서 -1로 만든다.
for i in range(5):
    total+=l[i]
    idx=copy.index(l[i])
    copy[idx]=-1
print(total)
#값이 -1인 경우에만 그 i+1을 출력 (~번째를 출력하는 것!)
for i in range(8):
    if copy[i]==-1:
        print(i+1,end=' ')