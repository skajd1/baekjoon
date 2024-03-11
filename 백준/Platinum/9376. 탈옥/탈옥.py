import sys
from collections import deque

input = sys.stdin.readline
t=int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def countDoors(board,h,w,i,j):
    chkRange = lambda x,y : True if 0<=x<h and 0<=y<w else False
    visited = [[-1] * w for _ in range(h)]
    visited[i][j] = 0 if board[i][j] != '#' else 1
    q = deque([[i,j]])
    while q :
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if chkRange(nx,ny) :
                if board[nx][ny] == '*' : continue
                if board[nx][ny] in ['$','.'] :
                    if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] :
                        visited[nx][ny] = visited[x][y]
                        q.append([nx,ny])
                if board[nx][ny] == '#' :
                    if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1 :
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx,ny])
    return visited
    

for _ in range(t):
    h,w = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]
    
    newBoard = [['.'] * (w+2)]
    for b in board:
        newBoard.append(['.'] + b + ['.'])
    newBoard.append(['.'] * (w+2))
    ans = 100001
    prisoner = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == '$' :
                prisoner.append([i,j])
    doorCount1 = countDoors(newBoard,h+2,w+2,prisoner[0][0]+1,prisoner[0][1]+1)
    doorCount2 = countDoors(newBoard,h+2,w+2,prisoner[1][0]+1,prisoner[1][1]+1)
    doorCount3 = countDoors(newBoard,h+2,w+2,0,0)

    for i in range(h+2):
        for j in range(w+2):
            if newBoard[i][j] == '*': continue
            if doorCount1[i][j] == -1 or doorCount2[i][j] == -1 or doorCount3[i][j] == -1 : continue
            cnt = doorCount1[i][j] + doorCount2[i][j] + doorCount3[i][j]
            if newBoard[i][j] == '#' : cnt -=2
            ans = min(ans, cnt)
    print(ans)