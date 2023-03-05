cnt=0
for i in range(5):
    a=int(input())
    if a <40:
        a=40
    cnt=cnt+a
print(int(cnt/5))