import sys

x,y=map(int,sys.stdin.readline().split())
z=y*100//x

#승률 100% ==이긴횟수== 경기횟수는 승률이 더이상오를 수 없음
#승률 99% == 단 한 번이라도 졌기에 승률이 100%가 될 수 없음
# 두 경우가 예외처리
if z>=99:
    print(-1)
else: #이진탐색
    result=0
    left,right=1,x
    while left<=right:
        mid=(left+right)//2 #중간값
        if (y+mid)*100//(x+mid) >z:
            result=mid
            right=mid-1
        else:
            left=mid+1
    print(result)