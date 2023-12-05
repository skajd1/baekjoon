import copy
from collections import deque
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# dfs로 기둥(1)을 지도상에 세우고 기둥 갯수 == 3일 때, 바이러스가 퍼지는 함수 써서 0의 갯수 max값 찾기
tmp = []
def dfs(N):
	global board,ans,tmp
	if N == 3 :
		ans = max(ans,virus(board))
		
		return
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0 and [i,j] not in tmp :
				if tmp :
					if (tmp[-1][0] * len(board)) + tmp[-1][1] > (i * len(board)) + j :
						continue
				tmp.append([i,j])
				board[i][j] = 1
				dfs(N+1)
				tmp.pop()
				board[i][j] = 0
a = []
def virus(board):
	global a
	b = copy.deepcopy(board)
	s = 0
	q = deque()
	dx = [1,-1,0,0]
	dy = [0,0,1,-1]
	for i in range(len(board)):
		for j in range(len(board[0])):
			if b[i][j] == 2 :
				q.append([i,j])
				while q:
					x,y = q.popleft()
					for k in range(4):
						nx = x + dx[k]
						ny = y + dy[k]
						if 0<=nx< len(b) and 0<= ny < len(b[0]) and b[nx][ny] == 0 :
							q.append([nx,ny])
							b[nx][ny] = 2
							
	for bb in b :
		s += bb.count(0)		
	return s
	

dfs(0)
print(ans)
