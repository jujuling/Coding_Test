import sys

for i in range(3):
    l=list(map(int,sys.stdin.readline().split()))

    cal=(l[3]*3600+l[4]*60+l[5])-(l[0]*3600+l[1]*60+l[2])
    s=cal%60
    m=(cal//60)%60
    h=cal//3600

    print(h,m,s)