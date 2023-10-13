n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
start = list(map(int, input().split()))
end = list(map(int, input().split()))
for i in range(3):
    start[i] -= 1
    end[i] -= 1
# 동서남북
# 0 1 2 3
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
leftdir = [3,2,0,1]
rightdir = [2,3,1,0]
from collections import deque

visited = [[[float('inf')] * 4 for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]][start[2]] = 0
q = deque([[start[0], start[1], start[2]]])
ans = -1
while q:
    x, y, dir = q.popleft()
    # 방향 전환
    if visited[x][y][leftdir[dir]] > visited[x][y][dir] + 1:
        visited[x][y][leftdir[dir]] = visited[x][y][dir] + 1
        q.append([x,y,leftdir[dir]])
    if visited[x][y][rightdir[dir]] > visited[x][y][dir] + 1:
        visited[x][y][rightdir[dir]] = visited[x][y][dir] + 1
        q.append([x,y,rightdir[dir]])
        
    # k = 1 2 3
    for k in range(1,4):
        nx = x + dx[dir]*k
        ny = y + dy[dir]*k
        if 0<=nx<n and 0<=ny < m and board[nx][ny] == 0:
            if visited[nx][ny][dir] > visited[x][y][dir] + 1:
                visited[nx][ny][dir] = visited[x][y][dir] + 1
                q.append([nx,ny,dir])          
        else :
            break
print(visited[end[0]][end[1]][end[2]])