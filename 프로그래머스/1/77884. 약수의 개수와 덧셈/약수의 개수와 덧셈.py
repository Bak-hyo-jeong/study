import numpy as np

def solution(left, right):
    answer = 0
            
    for i in range(left, right+1):
        if i % (i ** 0.5) == 0:
            answer -= i
        else :
            answer += i
            
    return answer

    # for i in range(left, right+1):
    #     o = 0
    #     for j in range(1, i+1):
    #         if i % j == 0:
    #             o += 1
    #     if o % 2 == 0:
    #         answer += i
    #     else :
    #         answer -= i