import sys

n=int(sys.stdin.readline())
result=0
for i in range(n):
    l=[]
    word=sys.stdin.readline().strip()
    check=0
    #반복문을 돌면서
    for j in range(len(word)):
        #현재 단어가 l 리스트에 있다면
        if word[j] in l:
            #만약 이전 단어가 같은지 확인하고, 같다면 l 리스트에 추가
            if word[j-1] == word[j]:
                l.append(word[j])
            else: #이전 단어가 다른 단어라면 check=1로 바꾸고 반복문종료
                check=1
                break
        else: #만약 현재 단어가 l에 없다면 추가하기
            l.append(word[j])

    if check==0:
        result+=1

print(result)