S=list(input())
l=[-1 for i in range(26)]

for i in range(len(S)):
    tmp=ord(S[i])-97
    if l[tmp] == -1:
        l[tmp]=i

print(*l)