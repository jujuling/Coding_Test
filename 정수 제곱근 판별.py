import math

def solution(n):
    answer = math.sqrt(n)
    if answer==int(answer):
        result = math.pow(answer+1,2)
        return int(result)
    else:
        return -1