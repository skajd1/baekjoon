import sys
from collections import deque
input = sys.stdin.readline
w,h = map(int, input().split())
board = [list(input().strip()) for _ in range(h)]


# 방향 전환을 최소로
dx = [-1,0,1,0]
dy = [0,1,0,-1]
startx = -1
starty = -1
endx = -1
endy = -1
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C' :
            if startx == -1 :
                startx = i
                starty = j
            else :
                endx = i
                endy = j
            
# 해당 칸을 지날 때의 방향에 따른 cnt 최소값 저장
# visited[i]j][k] = i,j칸을 k방향으로 지날 때의 cnt 최소값
visited = [[[-1] * 4 for _ in range(w)] for _ in range(h)]

q = deque()
for i in range(4):
    nx = startx + dx[i]
    ny = starty + dy[i]
    if 0<=nx<h and 0<=ny < w and board[nx][ny] != '*' :
        q.append([nx,ny,i,0])
        visited[nx][ny][i] = 0

while q :
    x,y,d,cnt = q.popleft()
    # d가 같은 경우와 d가 1차이만 날 때만
    # 방향 전환 시 cnt += 1 하고 d는 변경해서 q에 넣기
    # visited 업데이트
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<= ny < w and board[nx][ny] != '*' :
            if abs(d-i) == 2 :
                continue
            if i == d :
                if visited[nx][ny][i] == -1 or visited[nx][ny][i] > cnt :
                    visited[nx][ny][i] = cnt
                    q.append([nx,ny,i,cnt])
            else :
                if visited[nx][ny][i] == -1 or visited[nx][ny][i] > cnt + 1:
                    visited[nx][ny][i] = cnt + 1
                    q.append([nx,ny,i,cnt+1])
                    
print(min(list(filter(lambda x : x != -1 , visited[endx][endy]))))