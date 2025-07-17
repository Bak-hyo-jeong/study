def solution(myStr):
    answer = []
    dl = []
    tmp = ''
    
    for i in myStr:
        if i == "a" or i == "b" or i == "c":
            if tmp != "" :
                answer.append(tmp)
                tmp = ""
        else:
            tmp += i
            
    if tmp != "":
        answer.append(tmp)
        
    if answer == []:
        answer.append("EMPTY")
    
    return answer