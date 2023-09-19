# 1  2  3  4 
# 위 아 왼 오
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
# n 격자 크기
# m 상어 수
# k 냄새 양
n,m,k = map(int, input().split())
board = [[]*n for _ in range(n)]
smell = [[]*n for _ in range(n)] # [냄새 남은시간 , 냄새 뿌린 상어 번호]
for i in range(n):
    for num in list(map(int, input().split())) :
        board[i].append(num)
        if num > 0 :
            smell[i].append([k,num])
        else :
            smell[i].append([0,0])

directions = [0] + list(map(int, input().split()))
dirPrior = [[0]] # i번 상어의 방향 우선순위
for i in range(m):
    tmp = [0]
    for j in range(4):
        tmp.append(list(map(int, input().split())))
    dirPrior.append(tmp)

cnt = m # 남은 상어 수
# 1. 냄새 없는 칸
# 2. 자신의 냄새가 있는 칸
# 3. 우선순위 방향
# 냄새는 k번 이동 후 사라짐
# 1번 상어만 남을 때까지 반복
# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 지우기

def move():
    global cnt,board
    newBoard = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 :
                sharkNum = board[i][j]
                dir = directions[sharkNum]
                flag = 0
                # smell 이 없는 칸 먼저 탐색
                for k in range(4):
                    nextDir = dirPrior[sharkNum][dir][k]
                    nx = i + dx[nextDir]
                    ny = j + dy[nextDir]
                    if 0 <= nx < n and 0<= ny < n :
                        if smell[nx][ny][0] == 0 :
                            flag = 1
                            if newBoard[nx][ny] == 0 or newBoard[nx][ny] > sharkNum:
                                if newBoard[nx][ny] > sharkNum:
                                    cnt -= 1
                                newBoard[nx][ny] = sharkNum
                                directions[sharkNum] = nextDir
                            else:
                                cnt -= 1

                            break
                # 없으면 자신의 냄새가 있는 칸 탐색
                if flag == 0 :
                    for k in range(4):
                        nextDir = dirPrior[sharkNum][dir][k]
                        nx = i + dx[nextDir]
                        ny = j + dy[nextDir]
                        if 0 <= nx < n and 0<= ny < n and smell[nx][ny][1] == sharkNum:
                            newBoard[nx][ny] = sharkNum
                            directions[sharkNum] = nextDir
                            break
    board = newBoard

def initSmell():
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                smell[i][j][0] = k
                smell[i][j][1] = board[i][j]
                continue
            if smell[i][j][0] > 0:
                smell[i][j][0] -= 1
                if smell[i][j][0] == 0:
                    smell[i][j][1] = 0
t = 0
while cnt > 1 :
    if t>= 1000:
        t = -1
        break
    move()
    initSmell()
    t += 1

print(t)