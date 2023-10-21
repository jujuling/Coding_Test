import sys

t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    hak,gpa=0,0.0
    for j in range(n):
        c,g=map(float,sys.stdin.readline().split())
        hak+=int(c)
        gpa+=c*g
    print("%d %.1f" %(hak,gpa/hak))