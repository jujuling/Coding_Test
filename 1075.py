import sys

n=int(sys.stdin.readline())
f=int(sys.stdin.readline())

#뒤의 2자리를 최소부터 시작하기 위해 00으로 바꾸는 과정
n=(n//100)*100

#i가 1부터 99까지
for i in range(100):
    if n%f==0:
        n=str(n)
        break
    n+=1
print(n[-2:])