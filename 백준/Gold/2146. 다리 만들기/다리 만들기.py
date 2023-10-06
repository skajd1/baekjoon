from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
ans = 100000000
q = deque()
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            cnt += 1
            q.append([i, j])
            visited[i][j] = 1
            while q:
                x, y = q.popleft()
                board[x][y] = cnt
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        if board[nx][ny] == 1:
                            q.append([nx, ny])
                            visited[nx][ny] = 1
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            dist = [[-1] * n for _ in range(n)]
            q.append([i, j])
            dist[i][j] = 0
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                        if board[nx][ny] == 0:
                            dist[nx][ny] = dist[x][y] + 1
                        elif board[nx][ny] == board[i][j]:
                            dist[nx][ny] = 0
                        elif board[nx][ny] != board[i][j]:
                            ans = min(ans, dist[x][y])
                            q.clear()
                            break
                        q.append([nx, ny])

print(ans)