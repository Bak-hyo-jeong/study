def solution(arr, k): 
    answer = [-1] * k
    i = 0
    
    for n in arr:
        if n not in answer:
            if i < k:
                answer[i] = n
                i += 1
            else:
                break
            
    return answer