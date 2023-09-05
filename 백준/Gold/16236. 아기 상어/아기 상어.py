N = int(input())
space = []
curSize = 2
dx = [-1,0,0,1]
dy = [0,-1,1,0]

for n in range(N) :
    line = list(map(int,input().split()))
    space.append(line)
    for l in range(len(line)) :
        if space[n][l] == 9 :
            space[n][l] = 0
            cur_x, cur_y = n, l

def bfs(x,y) :
    global curSize
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    que = []
    que.append([x,y])
    arr = []
    while que :
        x,y = que.pop(0)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if visited[nx][ny] == 0 and space[nx][ny] <= curSize :
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    que.append([nx,ny])
                    if space[nx][ny] != 0 and space[nx][ny] < curSize :
                        arr.append([nx,ny,distance[nx][ny]])
    arr.sort(key=lambda x : (x[2],x[0],x[1]))
    return arr

answer,cnt = 0,0
while True :
    fishList = bfs(cur_x,cur_y)
    if len(fishList) == 0 :
        print(answer)
        break
    cur_x,cur_y,dist = fishList[0]
    cnt += 1
    if cnt == curSize :
        curSize += 1
        cnt = 0
    answer += dist
    space[cur_x][cur_y] = 0