s=int(input())
cnt=0
i=1
while 1:
    cnt = cnt + i
    if cnt>s:
        break
    i = i + 1
print(i-1)