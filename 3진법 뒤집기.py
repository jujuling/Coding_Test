def solution(n):
    three = []
    while n!=0:
        three.append(n % 3)
        n//=3
    leng=len(three)
    result=0
    for i in range(leng) :
        result += three[i]*(3**(leng-1-i))
    return result