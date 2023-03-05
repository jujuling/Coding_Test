t=int(input())
for _ in range(t):
    s=input()
    total=0
    cnt=0
    for i in s:
        if i=="O":
            cnt+=1
            total+=cnt
        else :
            cnt=0
    print(total)