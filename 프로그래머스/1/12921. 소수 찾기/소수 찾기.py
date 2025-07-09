

def solution(n):
    answer = 0
    table = set(range(2, n+1)) 
        
    for i in range(2, n+1):
        if i in table:
            table -= set(range(i+i, n+1, i))
    
    
    return len(table)
                
                #     for i in range(2, n+1):
#         si = int(i ** 0.5)
#         for j in range(2, si + 1):
#             if i % j == 0 :
#                 aa.append(i)
    
#         if i in aa:
#             aa.remove(i)
    
#     answer = n - len(aa) - 1