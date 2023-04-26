def solution(n):
    answer=0
    tmp=n
    while n!=0:
        answer+=n%10
        n//=10
    if tmp%answer ==0:
        return True
    else :
        return False