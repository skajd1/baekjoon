import sys

board = []
for _ in range(19):
    tmp = list(map(int, sys.stdin.readline().split()))
    board.append(tmp)

# 상하좌우 탐색이 아니라 ↗ → ↘ ↓  탐색을 해야함
dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]
flag = False

for x in range(19):
    for y in range(19):
        
        if board[x][y] != 0:
            num = board[x][y]

            for i in range(4):
                cnt = 1
                nx =  x + dx[i]
                ny =  y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == num:
                    cnt += 1
                    nx += dx[i]
                    ny += dy[i]

                    if cnt == 5:
                        if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == num:
                            break

                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == num:
                             break

                        flag = True
                        print(num)
                        print(x + 1, y + 1)
                        break
                        
                    
if flag == False:
    print(0)