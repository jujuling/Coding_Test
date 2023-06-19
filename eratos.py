import math
n=1000
# 0,1을 제외한 2~1000까지의 모든 수에 대하여 소수 판별
arr = [True for i in range(n+1)]

#2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2,int(math.sqrt(n))+1):
    #i가 소수인 경우( 남은 수인 경우 = True)
    if arr[i]:
        #i의 배수 모두 False로 변환
        #i 자체는 제거하지 않기 때문에 시작을 i+i로 주었다.
        for j in range(i+i, n+1, i):
            arr[j]=False

#모든 소수 출력
for i in range(2,n+1):
    if arr[i]:
        print(i,end=' ')
