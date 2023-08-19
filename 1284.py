import sys
s
while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    n=str(n)
    result=2+len(n)-1 #양끝값과 자리 사이의 여백 수 미리 저장
    for i in n:
        if i==str(0):
            result+=4
        elif i==str(1):
            result+=2
        else:
            result+=3
    print(result)