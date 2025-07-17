def solution(strArr):
    ca = {}
    
    for i in strArr:
        count = 0
        for j in i:
            count += 1
            
        if count in ca:
            ca[count] += 1
        else:
            ca[count] = 1
            
    max_count = 0
    for k in ca:
        if ca[k] > max_count:
            max_count = ca[k]
               
    return max_count