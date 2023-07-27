import sys

#식 입력받기
l=sys.stdin.readline().strip()
# '-' 문자 기준으로 문자열을 자른다.
l=l.split('-')
#만약 l의 길이가 1이라면 -가 없다는 뜻이므로
# + 계산만 하면 된다.
if len(l)==1:
    l=''.join(l) #리스트에서 다시 문자열로 저장해주고
    l=l.split('+') # '+' 문자 기준으로 문자열을 자른다.
    result=int(l[0])
    for i in range(1,len(l)): #전체 숫자들을 더하는 과정
        result+=int(l[i])
else: #문자열에 '-'가 있을 경우의 계산과정
    fl=[] # + 연산이 계산된 값을 저장할 최종 리스트
    for i in l: #기존 값들이 저장된 l 리스트를 돌면서
        # '+' 연산자가 있을 경우
        if '+' in i:
            hap=0 # + 연산을 해서 저장해줄 변수
            num=0 # 숫자만 저장할 변수
            for j in i:
                if j =='+': #반복문을 돌면서 +를 만날경우에
                    hap+=num #hap에 + 만나기전 숫자를 저장하고
                    num=0 #숫자 저장 변수는 초기화 해준다.
                else: # 문자가 + 가 아니라면
                    num *= 10 #num에다가 숫자를 저장한다.
                    num+=int(j)

            hap+=num #최종 더한 값을 저장하고
            fl.append(hap) #fl 리스트에 값을 추가한다.
        else: # '+' 연산자가 없을 경우 바로 fl에 값을 추가한다.
            fl.append(i)
    #최종 - 계산을 해주는 과정
    result=int(fl[0])
    for i in range(1,len(fl)):
        result-=int(fl[i])
print(result)