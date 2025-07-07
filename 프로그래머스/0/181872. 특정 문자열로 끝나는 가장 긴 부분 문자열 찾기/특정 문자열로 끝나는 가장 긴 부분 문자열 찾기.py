def solution(myString, pat):
    
    for i, v in enumerate(myString):
        for a, b in enumerate(pat):
            if v == b:
                answer = ''
                answer += myString[:i+1]
    
    return answer