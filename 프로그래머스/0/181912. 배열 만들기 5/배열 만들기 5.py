def solution(intStrs, k, s, l):
    answer = []
    a = ''
    
    for i in intStrs:
        ss = i[s:s+l]
        if int(ss) > k:
            answer.append(int(ss))
    
    return answer