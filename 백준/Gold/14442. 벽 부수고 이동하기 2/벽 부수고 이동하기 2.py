n,m,k = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
from collections import deque
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
q = deque([[0,0,0]])
visited[0][0][0] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = -1
while q:
    x,y,cnt = q.popleft()
    if x == n-1 and y == m-1 :
        ans = min(ans, visited[x][y][cnt]) if ans != -1 else visited[x][y][cnt]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == '0' and visited[nx][ny][cnt] == 0:
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                q.append([nx,ny,cnt])
            elif board[nx][ny] == '1' and cnt < k and visited[nx][ny][cnt+1] == 0:
                visited[nx][ny][cnt+1] = visited[x][y][cnt] + 1
                q.append([nx,ny,cnt+1])
print(ans)