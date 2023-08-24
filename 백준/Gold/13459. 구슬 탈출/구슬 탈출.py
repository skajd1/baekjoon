n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
rx,ry = 0,0
bx,by = 0,0
hx,hy = 0,0
delta = [[-1,0],[1,0],[0,-1],[0,1]]
ans = 0

# dfs로 depth 10까지 탐색
def dfs(cnt,red,blue,direction, redGoal,blueGoal):
    global ans
    if ans : return
    if cnt > 10 :  # depth 가 10이 넘어갈 때도 빨간 공이 구멍에 빠지지 않는다면 return
        return
    if blueGoal: # backtracking | 파란 공이 구멍에 빠진 경우
        return
    if redGoal : # 빨간 공만 구멍에 빠지면
        ans = 1
        return

    # 상 하 좌 우 탐색
    for i in range(4):
        nred, nblue,rg,bg = move(i,red,blue)
        dfs(cnt+1, nred,nblue,direction+[i],rg,bg)
def move(dir,red,blue): # dir 방향으로 기울인 후, 빨간 공과 파란 공의 위치 반환
    dx = delta[dir][0]
    dy = delta[dir][1]
    redCheck = 0
    blueCheck = 0
    redGoal = 0
    blueGoal = 0
    res_red = [red[0], red[1]]
    res_blue = [blue[0],blue[1]]
    rb = 0 # red먼저 0 blue 먼저 1
    # n,m 중에서 0행 0열 , n-1행, m-1열은 모두 벽
    # ***진행 방향에서 앞서 있는 공 먼저 움직여야함*** 
    # 이동 중에 구멍 있거나 벽 혹은 공을 만나면 그 위치 저장하고, Check변수 True 만들기
    # 둘다 True 되면 while문 종료 후 각 좌표 반환
    if dir == 0 :
        if res_red[0] < res_blue[0] : rb = 0
        else : rb = 1
    elif dir == 1 :
        if res_red[0] >= res_blue[0] : rb = 0
        else : rb = 1
    elif dir == 2:
        if res_red[1] < res_blue[1] : rb = 0
        else : rb = 1
    else :
        if res_red[1] >= res_blue[1] : rb = 0
        else : rb = 1   
    while (not redCheck or not blueCheck): # 공들이 멈출 때 까지 ~~   
        nred = [res_red[0] + dx, res_red[1] + dy]
        nblue = [res_blue[0] + dx, res_blue[1] + dy]
        if rb : # 파란 공 먼저
            if 1<=nblue[0] <n-1 and 1<=nblue[1] <m-1 and not board[nblue[0]][nblue[1]] == '#' :
                res_blue = [nblue[0], nblue[1]]
                if nblue[0] == hx and nblue[1] == hy :
                    blueCheck = 1
                    blueGoal = 1
            else :
                blueCheck = 1
            if 1<=nred[0] < n-1 and 1<=nred[1] < m-1 and not board[nred[0]][nred[1]] == '#' and not(res_blue[0] == nred[0] and res_blue[1] == nred[1]):
                res_red = [nred[0],nred[1]]
                if nred[0] == hx and nred[1] == hy :
                    redCheck = 1
                    redGoal = 1
            else :
                redCheck = 1
        else : # 빨간 공 먼저 
            if 1<=nred[0] < n-1 and 1<=nred[1] < m-1 and not board[nred[0]][nred[1]] == '#' :
                res_red = [nred[0],nred[1]]
                if nred[0] == hx and nred[1] == hy :
                    redCheck = 1
                    redGoal = 1
            else :
                redCheck = 1
            if 1<=nblue[0] <n-1 and 1<=nblue[1] <m-1 and not board[nblue[0]][nblue[1]] == '#' and not(res_red[0] == nblue[0] and res_red[1] == nblue[1]) :
                res_blue = [nblue[0], nblue[1]]
                if nblue[0] == hx and nblue[1] == hy :
                    blueCheck = 1
                    blueGoal = 1
            else :
                if nblue[0] == hx and nblue[1] == hy :
                    blueGoal = 1
                blueCheck = 1    
    return res_red, res_blue, redGoal, blueGoal


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R' :
            rx = i
            ry = j
            board[i][j] = '.'
        elif board[i][j] == 'B' :
            bx = i
            by = j
            board[i][j] = '.'
        elif board[i][j] == 'O':
            hx = i
            hy = j
            board[i][j] = '.'
        
dfs(0,[rx,ry],[bx,by],[],0,0)
print(ans)