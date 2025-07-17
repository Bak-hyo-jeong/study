def solution(rank, attendance):
    rr = []
    
    for i in range(len(rank)):
        if attendance[i] == True:
            rr.append((rank[i], i))
    
    rr = sorted(rr)[0:3]      
    a = rr[0][1]
    b = rr[1][1]
    c = rr[2][1]
    
    return 10000 * a + 100 * b + c