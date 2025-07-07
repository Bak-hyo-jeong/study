def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []
    an = []
    
    for i in range(n):
        a1.append(str(bin(arr1[i]))[2:].zfill(n))
        a2.append(str(bin(arr2[i]))[2:].zfill(n))
    

    for za, zb in zip(a1, a2):
        for i, j in zip(za, zb):
            if int(i) == 0 and int(j) == 0:
                answer += " "
            else:
                answer += "#"             
        an.append(''.join(answer))
        answer = ''
            
    
    return an