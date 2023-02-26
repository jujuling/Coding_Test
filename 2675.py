T=int(input())

for _ in range(T):
    R,S=input().split()
    S=list(S)
    P=""
    for i in range(len(S)):
        P=P+S[i]*int(R)
    print(P)