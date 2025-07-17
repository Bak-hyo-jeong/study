def solution(picture, k):
    answer = []
    
    for i in picture:
        n = ""
        for j in i:
            n += j * k
    
        for _ in range(k):
            answer.append(n)
            
    return answer