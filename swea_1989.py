T = int(input())
for test_case in range(1, T + 1):
    s=input()
    if s[:] == s[::-1]:
        result=1
    else:
        result=0

    print("#%d %d" %(test_case,result))