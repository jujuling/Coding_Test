import sys

while True:
    w=sys.stdin.readline().rstrip()
    #종료 조건
    if len(w)==1 and w=='.':
        break
    #괄호를 받을 스택
    st=[]
    #flag는 문자열에서 괄호가 있는지 세는 인덱스
    flag=0
    #popnum은 pop한 개수 세는 인덱스
    popnum=0
    #realout은 닫는 괄호가 나올 때,
    #스택에 남아있는 문자가 없어서 break되는 경우를 저장하기 위한 인덱스
    realout=0
    #기본값은 no라고 설정함
    result="no"
    for i in range(len(w)):
        #반복문을 돌면서 여는 괄호가 나오면 스택에 추가함
        if w[i]=='(' or w[i]=='[':
            flag+=1
            st.append(w[i])
        #입력값이 ')'인 경우에
        elif w[i]==')':
            flag+=1
            #스택값이 없다면 realout
            if len(st)==0:
                realout=1
                break
            #스택의 젤 위의 값이 여는괄호라면 짝을 이뤄, pop해줌
            if st[-1]=='(':
                popnum+=1
                st.pop()
            else: #스택 젤 위의 값이 여는 괄호가 아닌 다른 값이라면 break
                break
        # 입력값이 ']'인 경우에
        elif w[i]==']':
            flag+=1
            # 스택값이 없다면 realout
            if len(st)==0:
                realout=1
                break
            # 스택의 젤 위의 값이 여는괄호라면 짝을 이뤄, pop해줌
            if st[-1]=='[':
                popnum+=1
                st.pop()
            else: #스택 젤 위의 값이 여는 괄호가 아닌 다른 값이라면 break
                break
    #만약에 괄호의 갯수가 0이라면 괄호가 없는 문자열이므로 균형잡힌 문자열임
    if flag==0:
        result="yes"
    if realout==1:
        result="no"
    else:
        #pop을 정상적으로 수행하여 스택이 깔끔하게 비워진 경우, 균형잡힌 문자열
        if popnum!=0 and len(st)==0:
            result = "yes"
    print(result)