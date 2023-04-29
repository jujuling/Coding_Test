def solution(s):
    if len(s)==4 or len(s)==6:
        answer=True
    else:
        return False
    for i in s:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            answer = False
    return answer