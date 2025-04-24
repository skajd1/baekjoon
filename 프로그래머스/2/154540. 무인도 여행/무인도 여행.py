dx = [1,-1,0,0]
dy = [0,0,1,-1] 
from collections import deque

def solution(maps):
    answer = []
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    chkRange = lambda x,y : True if 0<=x<len(maps) and 0<=y<len(maps[0]) else False
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                
                visited[i][j] = 1
                q = deque([[i,j]])
                now = int(maps[i][j])
                
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if chkRange(nx,ny) and not visited[nx][ny] and maps[nx][ny] != 'X':
                            visited[nx][ny] = 1
                            now += int(maps[nx][ny])
                            q.append([nx,ny])
                                       
                answer.append(now)
    
    
    return sorted(answer) if answer else [-1]