def solution(n):
    answer = [[0] * n  for _ in range(n)]
    
    x, y, dir = 0, 0, 0
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for i in range(1, n*n +1):
        answer[x][y] = i
        
        nx, ny = x + dx[dir], y + dy[dir]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n or answer[nx][ny]!=0:
            dir = (dir + 1) % 4
            nx, ny = x + dx[dir], y + dy[dir]
            
        x, y = nx, ny
        
    return answer