T=int(input())

for test_case in range(1,T+1):
    n=list(input())
    print(n)
    result=0
    first=list(0 for i in range(len(n)))
    print(first)
    for i in range(len(first)):
        if int(n[i])!=first[i]:
            for j in range(i,len(first)):
                first[j]=int(n[i])
            result+=1
            print(first)
        else:
            continue

    print("#%d %d" %(test_case,result))