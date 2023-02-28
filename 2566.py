l= [[0 for col in range(9)] for row in range(9)]
for i in range(9):
    l[i]=list(map(int,input().split()))

tmp=[]
for i in range(9):
    tmp.append(max(l[i]))
total=max(tmp)

resulti=0
resultj=0
for i in range(9):
    for j in range(9):
        if (l[i][j]==total):
            resulti=i
            resultj=j

print(total)
print(resulti+1,resultj+1)