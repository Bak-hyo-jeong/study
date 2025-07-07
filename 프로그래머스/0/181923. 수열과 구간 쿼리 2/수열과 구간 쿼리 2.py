def solution(arr, queries):    
    answer = []   

    for s, e, k in queries:
        w = []
        for i in range(s, e+1):
            if arr[i] > k:
                w.append(arr[i])
        if w:
            answer.append(min(w))
        else:
            answer.append(-1)
    return answer