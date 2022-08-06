A=int(input())
B=int(input())
C=int(input())
gob = A*B*C
g_list = list(map(int,str(gob)))

result = [0,0,0,0,0,0,0,0,0,0]

for i in range(9) :
    for j in range(len(g_list)):
        if i == g_list[j] :
            result[i] +=1
i=0
for i in range(10):
    print(result[i])
