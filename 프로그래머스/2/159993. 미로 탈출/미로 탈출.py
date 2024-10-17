from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def fromStartToLever(maps,i,j):
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[i][j] = 1
    q = deque([[i,j,0]])
    while q :
        x,y,now = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and not visited[nx][ny] :
                visited[nx][ny] = 1
                if maps[nx][ny] == "L" : return fromLeverToExit(maps,nx,ny,now+1)
                if maps[nx][ny] != "X" : q.append([nx,ny,now+1])
    return -1

def fromLeverToExit(maps,i,j,t):
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[i][j] = 1
    q = deque([[i,j,t]])
    while q :
        x,y,now = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and not visited[nx][ny] :
                visited[nx][ny] = 1
                if maps[nx][ny] == "E" : return now+1
                if maps[nx][ny] != "X" : q.append([nx,ny,now+1])
    return -1
def solution(maps):
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S" :
                return fromStartToLever(maps,i,j)
    return -1