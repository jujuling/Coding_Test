for i in range(10):
    index=int(input())
    find=input()
    str=input()
    result=0
    for i in range(len(str)):
        if str[i] == find[0]:
            if str[i:i+len(find)] == find:
                result+=1

    print("#%d %d" %(index,result))