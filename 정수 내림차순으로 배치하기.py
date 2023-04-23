def solution(n):
    tmp=list(str(n))
    tmp.sort()
    tmp.reverse()
    answer=''.join(tmp)
    return int(answer)