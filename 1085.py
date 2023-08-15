import sys

x,y,w,h=map(int,sys.stdin.readline().split())

garo=h-y
r_garo=abs(y)
sero=w-x
r_sero=abs(x)
print(min(garo,r_garo,sero,r_sero))