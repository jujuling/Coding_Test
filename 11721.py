import sys

w=sys.stdin.readline().strip()
n=len(w)
flag=0
for i in range(n):
    if flag==10:
        flag=0
        print()
    print(w[i],end='')
    flag+=1