def solution(a, d, included):
    answer = 0
    
    for i in range(len(included)):
        if included[i] == 1:
            answer += a + d * i
    
    return answer