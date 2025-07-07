def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if len(arr) <= 2**i:
            answer += arr + [0]*(2**i - len(arr))
            break            
    
    return answer