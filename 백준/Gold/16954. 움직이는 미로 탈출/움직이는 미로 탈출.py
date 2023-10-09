from collections import deque
def moveWall():
    global board,cnt
    for i in range(7,-1,-1):
        for j in range(8):
            if board[i][j] == '#' :
                board[i][j] = '.'
                if i == 7 :
                    continue
                if board[i+1][j] == '0':
                    cnt -= 1
                    if cnt == 0 :
                        print(0)
                        exit(0)
                board[i+1][j] = '#'

board = [list(input().strip()) for _ in range(8)]
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
board[7][0] = '0'
cnt = 1
q = deque()
while cnt :
    tmp = 0
    for b in board:
        if '#' in b:
            break
        else:
            tmp += 1
    if tmp == 8:
        print(1)
        exit(0)

    for i in range(8):
        for j in range(8):
            if board[i][j] == '0':
                q.append((i,j))
    while q:   
        x,y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<8 and 0<=ny<8 and board[nx][ny] == '.':
                if nx == 0 and ny == 7 :
                    print(1)
                    exit(0)
                board[nx][ny] = '0'
                cnt += 1
                
    moveWall()