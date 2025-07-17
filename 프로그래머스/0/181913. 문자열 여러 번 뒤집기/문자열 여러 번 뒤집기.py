def solution(my_string, queries):

    answer = list(my_string)
    
    for i in queries:
        s, e = i
        answer[s:e+1] = answer[s:e+1][::-1]
    
    return ''.join(answer)