def solution(arr):
    answer = []
    a = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            a.append(i)
    
    if a:
        answer = arr[min(a):max(a)+1]
    else:
        return [-1]
    
    return answer