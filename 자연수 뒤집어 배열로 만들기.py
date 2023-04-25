def solution(n):
    answer=list()
    while n!=0:
        answer.append(n%10)
        n//=10
    return answer