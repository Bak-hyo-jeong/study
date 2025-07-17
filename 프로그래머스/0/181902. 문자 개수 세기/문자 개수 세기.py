def solution(my_string):
    answer = []
    
    for i in range(0, 52):
        answer.append(0)
    
    for m in my_string:
        for i in range(65, 91):
            if chr(i) in m:
                answer[i-65] += 1
    
        for i in range(97, 123):
            if chr(i) in m:
                answer[i-71] += 1
        
    return answer