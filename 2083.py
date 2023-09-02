import sys
while True:
    l=list(map(str,sys.stdin.readline().strip().split()))
    if l==['#','0','0']:
        break
    if int(l[1])>17 or int(l[2])>=80:
        print(l[0],"Senior")
    else:
        print(l[0],"Junior")