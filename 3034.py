import sys

n,w,h=map(int,sys.stdin.readline().split())
for i in range(n):
    tmp=int(sys.stdin.readline())
    if tmp <=w or  tmp <=h or tmp**2 <= (w**2 + h**2):
        print("DA")
    else:
        print("NE")