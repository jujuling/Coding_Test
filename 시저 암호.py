def solution(s, n):
    answer = ''
    for i in s:
        if i==' ':
            answer+=' '
        elif i>='a'and i<='z':
            if ord(i)+n>ord('z'):
                answer+=chr(ord(i)+n-26)
            else :
                answer += chr(ord(i) + n)
        elif i>='A' and i<='Z':
            if ord(i)+n>ord('Z'):
                answer+=chr(ord(i)+n-26)
            else :
                answer += chr(ord(i) + n)
        else:
            answer+=chr(ord(i)+n)
    return answer