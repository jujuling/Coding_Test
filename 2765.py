import sys

flag = 1
while True:
    r,c,t=map(float,sys.stdin.readline().split())
    if c==0:
        break
    #거리 = pi*r * c
    #pi = 3.1415927 로 설정
    #거리 계산 값은 inch 이나 mile로 결과값을 나타내야 함
    #1마일 = 5280 피트, 1피트 12인치이므로
    #1마일 == 63360 인치이다.
    dis=(3.1415927 * r * c)/63360

    #t는 초로 주어지고, 속도 계산은 시간으로 해야함
    #1시간=60분, 1분 =60초
    #1시간 =3600초
    mph=dis/(t/3600)
    print("Trip #%d: %.2f %.2f" %(flag,dis,mph))
    flag+=1