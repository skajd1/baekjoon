from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
size = 2
sizecnt = 0
shark = []
ans = 0
x,y = 0,0
for i in range(n):
	for j in range(n):
		if board[i][j] == 9 :
			x = i
			y = j
			board[i][j] = 0
def bfs(x,y,s):
	q = deque()
	q.append([x,y])
	distance = [[0] * n for _ in range(n)]
	visited = [[0] * n for _ in range(n)]
	visited[x][y] = 1
	candidate= []
	while q :
		xx,yy = q.popleft()
		dx = [1,-1,0,0]
		dy = [0,0,1,-1]
		for i in range(4):
			nx = xx + dx[i]
			ny = yy + dy[i]
			if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
				if board[nx][ny] <= s :
					q.append([nx,ny])
					visited[nx][ny] = 1
					distance[nx][ny] = distance[xx][yy] + 1
					if 0<board[nx][ny]<s :
						candidate.append([nx,ny,distance[nx][ny]])
	
	return sorted(candidate,key = lambda x : (-x[2],-x[0],-x[1]))

while (1):
	if len(arr := bfs(x,y,size)) :
		x,y,z = arr.pop()
		ans +=z
		board[x][y] = 0
		sizecnt += 1
		if sizecnt == size :
			size += 1
			sizecnt = 0
		
	else :
		print(ans)
		break
	