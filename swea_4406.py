T=int(input())

for test_case in range(1,T+1):
    s=list(input())
    result=list()
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            continue
        else:
            result.append(s[i])
    result="".join(result)
    print("#%d %s"  %(test_case,result))