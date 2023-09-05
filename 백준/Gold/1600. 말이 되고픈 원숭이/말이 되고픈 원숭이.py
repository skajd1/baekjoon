from collections import deque

# 입력값
k = int(input())
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우, 체스 나이트 이동
dist = [[1,0],[0,1],[-1,0],[0,-1]]
horse = [[-2,-1], [-2,1],[-1,-2],[-1,2],[2,-1],[2,1],[1,-2],[1,2]]

def bfs() :
    que = deque()
    que.append([0,0,0])
    visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while que :
        x,y,z = que.popleft()
        if x == n-1 and y == m-1 :
            return visited[x][y][z] - 1
        for (i,j) in dist :
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][z] and not graph[nx][ny] :
                visited[nx][ny][z] = visited[x][y][z] + 1
                que.append([nx,ny,z])
        if k > z :
            for (hx,hy) in horse :
                n_hx = x + hx
                n_hy = y + hy
                if 0 <= n_hx < n and 0 <= n_hy < m :
                    if not graph[n_hx][n_hy] :
                        if not visited[n_hx][n_hy][z+1] :
                            visited[n_hx][n_hy][z+1] = visited[x][y][z] + 1
                            que.append([n_hx,n_hy,z+1])
    return -1

print(bfs())