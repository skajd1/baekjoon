from collections import deque
dx = [-1,0,0,1]
dy = [0,-1,1,0]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
t = 0

# 현재 상어 크기와 같은 수 만큼의 물고기를 먹으면 상어 크기가 1 증가한다.
shark_size = 2
size_cnt = 0

sharkX, sharkY = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sharkX, sharkY = i, j
            board[i][j] = 0

def eatFish():
    global size_cnt, shark_size
    size_cnt += 1
    if shark_size == size_cnt :
        shark_size += 1
        size_cnt = 0

def findNearestFish():
    global t, board, sharkX, sharkY
    
    # bfs로 현재 상어 위치로부터 먹을 수 있는 가장 가까운 물고기.
    # 먹을 수 있는 물고기가 없으면 -1 리턴
    # 있으면 그 물고기 까지 가는 시간 리턴
    # 현재 상어 크기 미만의 물고기만 먹을 수 있음.
    # 빈칸과 현재 상어 크기 이하의 물고기 칸만 지나갈 수 있음
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((sharkX, sharkY,0))
    visited[sharkX][sharkY] = 1
    candidate = []
    while q:
        x,y,time = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny < n and not visited[nx][ny] :
                visited[nx][ny] = 1
                if board[nx][ny] > shark_size:
                    continue
                elif board[nx][ny] < shark_size and board[nx][ny] != 0:
                    candidate.append((nx,ny,time+1))
                elif board[nx][ny] == shark_size or board[nx][ny] == 0 :
                    q.append((nx,ny,time+1))
    if candidate :
        candidate.sort(key=lambda x:(x[2],x[0],x[1]))
        board[candidate[0][0]][candidate[0][1]] = 0
        sharkX = candidate[0][0]
        sharkY = candidate[0][1]
        eatFish()
        return candidate[0][2]
    return -1
                

while (x :=findNearestFish()) != -1:
    t += x
    
print(t)