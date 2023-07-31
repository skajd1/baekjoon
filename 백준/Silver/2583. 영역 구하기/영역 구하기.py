from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m, k = map(int, input().split())
arr = [[1] * m for _ in range(n)]
ans = []


def makeZero(x1, y1, x2, y2):
	pass
	for i in range(x1, x2):
		for j in range(y1, y2):
			arr[i][j] = 0


for y1, x1, y2, x2 in [map(int, input().split()) for _ in range(k)]:
	makeZero(x1, y1, x2, y2)

for i in range(n):
	for j in range(m):
		if arr[i][j]:
			q = deque([[i, j]])
			arr[i][j] = 0
			tmp = 1
			#bfs
			while q:
				x, y = q.popleft()
				for ii in range(4):
					nx = x + dx[ii]
					ny = y + dy[ii]
					if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]:
						tmp += 1
						arr[nx][ny] = 0
						q.append([nx, ny])
			ans.append(tmp)
print(len(ans))
print(*sorted(ans))
