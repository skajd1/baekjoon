import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
n,m = map(int,input().split())
cnt = 0
viruses = []
board = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
	for j in range(n):
		if board[i][j] == 2:
			viruses.append((i,j))
			board[i][j] = '*' # 바이러스
		if board[i][j] == 1:
			board[i][j] = '#' # 벽
		if board[i][j] == 0:
			cnt += 1
dx = [0,0,-1,1]
dy = [1,-1,0,0]
if cnt == 0:
	print(0)
	exit()
ans = -1
for comb in combinations(viruses,m):
	copied = [board[i][:] for i in range(n)]
	for x,y in comb:
		copied[x][y] = -1
		q = deque([[x,y,0]])
		while q :
			xx,yy,d = q.popleft()
			for i in range(4):
				nx = xx + dx[i]
				ny = yy + dy[i]
				if 0<=nx<n and 0<=ny<n:
					if copied[nx][ny] == '#':
						continue
					if copied[nx][ny] == '*':
						copied[nx][ny] = -1
						q.append([nx,ny,d+1])
					elif copied[nx][ny] == 0 or copied[nx][ny] >d+1:
						copied[nx][ny] = d+1
						q.append([nx,ny,d+1])
	dist = 0
	flag = True
	for i in range(n):
		if not flag:
			break
		for j in range(n):
			if copied[i][j] != '#' and copied[i][j] != '*':
				if copied[i][j] == 0 :
					flag = False
					break
				dist = max(dist,copied[i][j])
	if flag:
		if ans == -1:
			ans = dist
		else :
			ans = min(ans,dist)

print(ans)