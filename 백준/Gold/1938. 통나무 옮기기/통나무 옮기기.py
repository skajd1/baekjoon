n = int(input())
board = [list(input().strip()) for _ in range(n)]
dir = 0
centerx,centery=-1,-1

edir = 0
ecenterx,ecentery=-1,-1

for i in range(n):
    for j in range(n):
        if board[i][j] == 'B':
            if i+1 < n and board[i+1][j] == 'B' :
                dir = 1
                centerx,centery = i+1,j
                board[i][j] = '0'
                board[i+1][j] = '0'
                board[i+2][j] = '0'
            elif j+1 < n and board[i][j+1] == 'B' :
                centerx,centery = i,j+1
                board[i][j] = '0'
                board[i][j+1] = '0'
                board[i][j+2] = '0'
            break
        elif board[i][j] == 'E':
            if i+1 < n and board[i+1][j] == 'E' :
                edir = 1
                ecenterx,ecentery = i+1,j
                board[i][j] = '0'
                board[i+1][j] = '0'
                board[i+2][j] = '0'
            elif j+1 < n and board[i][j+1] == 'E' :
                ecenterx,ecentery = i,j+1
                board[i][j] = '0'
                board[i][j+1] ='0'
                board[i][j+2] = '0'
            break
# 가로 : 0, 세로 : 1
from collections import deque
q = deque([[centerx,centery,dir,0]])
visited = [[[0]*2 for _ in range(n)] for _ in range(n)]
visited[centerx][centery][dir] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0
def checkU(x,y,d):
    if d == 0 :
        if x-1 < 0 : return False
        for i in range(y-1,y+2):
            if board[x-1][i] != '0':
                return False    
    else :
        if x-2 < 0 : return False
        if board[x-2][y] != '0' : return False
    return True
def checkD(x,y,d):
    if d == 1 :
        if x+2 >= n : return False
        if board[x+2][y] != '0' : return False
    else :
        if x+1 >= n : return False
        for i in range(y-1,y+2):
            if board[x+1][i] != '0':
                return False
    return True
def checkL(x,y,d):
    if d == 0 :
        if y-2 < 0 : return False
        if board[x][y-2] != '0' : return False
    else :
        if y-1 < 0 : return False
        for i in range(x-1,x+2):
            if board[i][y-1] != '0':
                return False
    return True
def checkR(x,y,d):
    if d == 0 :
        if y+2 >= n : return False
        if board[x][y+2] != '0' : return False
    else :
        if y+1 >= n : return False
        for i in range(x-1,x+2):
            if board[i][y+1] != '0':
                return False
    return True
def checkT(x,y):
    # x,y 기준 3*3 아무것도 없어야함
    if x-1 < 0 or y-1 < 0 or x+1 >= n or y+1 >= n:
        return False
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if board[i][j] != '0':
                return False
    return True
while q:
    x,y,d,cnt = q.popleft()
    if x == ecenterx and y == ecentery and d == edir:
        ans = min(cnt,ans) if ans != 0 else cnt
        continue
    if checkU(x,y,d) and visited[x-1][y][d] == 0:
        visited[x-1][y][d] = 1
        q.append([x-1,y,d,cnt+1])
    if checkD(x,y,d) and visited[x+1][y][d] == 0:
        visited[x+1][y][d] = 1
        q.append([x+1,y,d,cnt+1])
    if checkL(x,y,d) and visited[x][y-1][d] == 0:
        visited[x][y-1][d] = 1
        q.append([x,y-1,d,cnt+1])
    if checkR(x,y,d) and visited[x][y+1][d] == 0:
        visited[x][y+1][d] = 1
        q.append([x,y+1,d,cnt+1])
    if checkT(x,y) and visited[x][y][1-d] == 0:
        visited[x][y][1-d] = 1
        q.append([x,y,1-d,cnt+1])
print(ans)