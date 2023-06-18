import sys

t=int(sys.stdin.readline())

for i in range(t):
    result = "NO"
    #괄호들을 저장할 리스트
    h = []
    tmp=sys.stdin.readline().rstrip()

    for j in range(len(tmp)):
        #만약 입력값이 ) 일때
        if tmp[j]==')':
            #h리스트에 값이 있고,
            if len(h)!=0:
                #앞의 값이 (라면 VPS이므로 (을 삭제함
                #()가 만들어져서 리스트에서 사라진 것으로 이해하면 됨
                if h[-1]=='(':
                    h.pop()
                #앞의 값이 ) 라면 현재값을 리스트에 추가
                else:
                    h.append(tmp[j])
            #h리스트에 값이 없다면 VPS를 만들 수 있는지 판별이 안되므로 ) r값 추가
            else:
                h.append(tmp[j])
        #입력값이 (라면 그냥 리스트에 추가해주면 됨
        else:
            h.append(tmp[j])
    #VPS 인지 확인 작업이 끝난후에 h리스트에 값이 없다면 모두 VPS이므로, YES
    if len(h)==0:
        result="YES"
    print(result)