from collections import deque
from copy import deepcopy
n,m = map(int, input().split())
bing = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0
def melt():
    global bing
    bing_copy = deepcopy(bing)
    flag = False
    for i in range(n):
        for j in range(m):
            if bing[i][j] :
                flag = True
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<m and bing[nx][ny] == 0:
                        bing_copy[i][j] -= 1
                        if bing_copy[i][j] == 0 : break
    bing = bing_copy
    return flag
def check():
    #bfs로 덩이 체크
    visited = [[0] * m for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(m):
            if bing[i][j] and not visited[i][j] :
                tmp += 1
                if tmp > 1 :
                    return False  
                q = deque([[i,j]])
                visited[i][j] = 1
                while q :
                    x,y = q.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny < m and bing[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append([nx,ny])

    return True               

while check() :
    ans += 1
    if(not melt()):
        ans = 0
        break
print(ans)