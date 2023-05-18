T=int(input())

for test_case in range(1,T+1):
    s=list(map(str,input()))
    tmp=[]

    for i in range(1,11):
        if s[:i]==s[i:2*i]:
            print("#%d %d" %(test_case,i))
            break