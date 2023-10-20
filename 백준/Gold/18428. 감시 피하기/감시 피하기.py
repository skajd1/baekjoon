n = int(input())
board = [list(input().strip().split()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
obj = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(cnt,x,y):
    global obj, visited
    if cnt == 3 :
        # 3개 벽을 세웠을 때 
        new_board = [board[i][:] for i in range(n)]
        for i,j in obj :
            new_board[i][j] = "O"
        for i in range(n):
            for j in range(n):
                if new_board[i][j] == "T" :
                    # 상하좌우 탐색
                    for k in range(4):
                        tmp = 0
                        while(True):
                            tmp += 1
                            nx = i + dx[k] * tmp
                            ny = j + dy[k] * tmp
                            if nx < 0 or nx >= n or ny < 0 or ny >= n or new_board[nx][ny] == "O":
                                break
                            if new_board[nx][ny] == "S" :
                                return            
        print("YES")
        exit(0)
    for i in range(n):
        for j in range(n):
            if i < x :
                continue
            if i == x and j <= y :
                continue
            if not visited[i][j] and board[i][j] == "X" :
                visited[i][j] = 1
                obj.append([i,j])
                dfs(cnt+1,i,j)
                visited[i][j] = 0
                obj.pop()


dfs(0,-1,1)
print("NO")