import sys

n,c=map(int,sys.stdin.readline().split())
l=[]
for i in range(n):
    l.append(int(sys.stdin.readline()))
#이진 탐색은 정렬이 필수
l.sort()

#집 사이에 최소 거리와 최대거리를 먼저 찾고,
#공유기들을 공평하게 설치할 수 있는 간격을 찾아 나가야한다.
#간격 찾기에 이진 탐색을 적용
#최소거리는 1, 최대거리는 리스트마지막값-첫번째값
start=1
end=l[n-1]-l[0]
result=0

while start <= end:
    mid = (start + end) // 2 #현재 기준 간격으로 설정
    #print(start,end,mid)
    # 첫집부터 공유기 설치 1개인 상황임
    current = l[0]
    cnt = 1

    #공유기 사이 간격을 돌면서
    for i in range(n):
        if l[i]-current>=mid: #간격이 기준보다 넓으면 공유기를 설치할 수 있음
            cnt+=1 #갯수 증가하고 현 위치로 current값을 바꿈
            current=l[i]
    if cnt>=c: #만약 공유기가 모두 설치가능하다면 간격을 늘린다.
        result=mid
        start=mid+1
    else: #공유기ㅏ 설치가 모두 설치 불가능할 경우에는 간격을 좁힌다.
        end=mid-1
print(result)