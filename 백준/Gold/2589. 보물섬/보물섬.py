import sys

r, c = map(int,sys.stdin.readline().split())
board = []
for _ in range(r) :
    line = list(sys.stdin.readline().rstrip())
    board.append(line)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0

def bfs(x,y) :
    que = []
    que.append([x,y])
    visited[x][y] = 1
    cnt = 0
    while que :
        x, y = que.pop(0)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c :
                if visited[nx][ny] == 0 and board[nx][ny] == 'L' :
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    que.append([nx,ny])
                    cnt = max(cnt,dist[nx][ny])
    return cnt

# L인 모든 행, 열 돌면서 visited 초기화 해주고, 최단거리 max로 초기화
for i in range(r) :
    for j in range(c) :
        if board[i][j] == 'L' :
            visited = [[0] * c for _ in range(r)]
            dist = [[0] * c for _ in range(r)]
            answer = max(answer,bfs(i,j))
print(answer)