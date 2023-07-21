from heapq import heappop, heappush
n,m = map(int, input().split())
height = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]* m for _ in range(n)]

# 상 하 좌 우
delta = ((-1,0),(1,0),(0,-1),(0,1))


# 각 칸으로 이동 시 조건 : 현재 칸보다 낮은 칸으로

# 이동할 때 마다 이동할 칸 dp 업데이트

# 탐색은 bfs로 현재 칸에서 이동할 수 있는 칸 queue에 넣고 돌리기

# dp[-1][-1] 출력


q = [[-height[0][0],0,0]]
dp[0][0] = 1
while q :
    h,x,y = heappop(q)
    for i in range(4):
        nx = x + delta[i][0]
        ny = y + delta[i][1]
        # 경계조건 & 현재 칸보다 낮으면
        if 0<=nx<n and 0<=ny < m and height[x][y] > height[nx][ny] :
            if not dp[nx][ny] :
                heappush(q, [-height[nx][ny],nx,ny])
            dp[nx][ny] += dp[x][y]

print(dp[-1][-1])


        