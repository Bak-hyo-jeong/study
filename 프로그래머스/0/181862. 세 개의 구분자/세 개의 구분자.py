def solution(myStr):
    answer = []
    tmp = ''
    
#     for i in myStr:
#         if i == "a" or i == "b" or i == "c":
#             if tmp != "" :
#                 answer.append(tmp)
#                 tmp = ""
#         else:
#             tmp += i
            
#     if tmp != "":
#         answer.append(tmp)
        
#     if answer == []:
#         answer.append("EMPTY")
    
    for ch in myStr:
        if ch in 'abc':
            if tmp:
                answer.append(tmp)
                tmp = ''
        else:
            tmp += ch
    if tmp:
        answer.append(tmp)
    
    return answer if answer else ["EMPTY"]