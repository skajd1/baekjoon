from collections import deque

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
n = int(input())
stick = list(map(int, input().split()))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()

def merge():
    global board
    visited= [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'x' and not visited[i][j]:
                lowest = i
                cluster = []
                q.append([i,j])
                visited[i][j] = 1
                while q :
                    x,y = q.popleft()
                    cluster.append([x,y])
                    lowest = max(lowest, x)
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] == 'x':
                            q.append([nx,ny])
                            visited[nx][ny] = 1
                if lowest == r-1:
                    continue
                else :
                    flag = True
                    cluster.sort(key=lambda x: -x[0])
                    board_copy = [b[:] for b in board]
                    while True:
                        for ii in range(len(cluster)):
                            x,y = cluster[ii]
                            if x + 1 < r and board_copy[x+1][y] == '.': #떨어질 수 있음
                                
                                board_copy[x][y] = '.'
                                board_copy[x+1][y] = 'x'
                                cluster[ii][0] += 1
                            else :
                                flag = False
                                break
                        if flag :
                            board = [b[:] for b in board_copy]
                        else : break
                    return
for i in range(n):
    if i % 2 == 0 :
        #left
        for j in range(c):
            if board[-stick[i]][j] == 'x':
                board[-stick[i]][j] = '.'
                merge()
                break
    else :
        #right
        for j in range(c-1,-1,-1):
            if board[-stick[i]][j] == 'x':
                board[-stick[i]][j] = '.'
                merge()
                break

for b in board:
    print(*b, sep='')