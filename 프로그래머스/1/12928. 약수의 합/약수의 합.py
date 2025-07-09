def solution(n):
  #  answer = 0
    sn = int(n ** 0.5)
    aa = []
    aa = set()
    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         answer += i              
    
    for i in range(1, sn+1):
        if n % i == 0:
            aa.add(i)
            aa.add(n // i)
         
    return sum(aa)