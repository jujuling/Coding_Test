import sys

m=list(sys.stdin.readline().strip())
s=[] #스택
result=0
for i in range(len(m)):
    if m[i]=='(':
        s.append(m[i])
    else: #m[i]==')'
        if m[i-1]=='(': #레이저인 경우
            s.pop()
            result+=len(s)
        else:
            s.pop()
            result+=1
print(result)