n=int(input())
l=list(map(int, input().split()))

cnt=0
for i in l :
    flag = 0
    for j in range(1,i+1):
        if i%j==0:
            flag=flag+1
    if flag==2:
        cnt=cnt+1
print(cnt)