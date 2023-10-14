T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
class cell :
	def __init__(self,life):
		self.life = life
		self.now = 0
		self.active = False
		self.dead = False
		
def simulate(cells):
	spread = []
	for i in range(len(cells)):
		for j in range(len(cells[0])):
		
			if cells[i][j] == 0 or cells[i][j].dead : continue
			if not cells[i][j].active:
				cells[i][j].now += 1
				if cells[i][j].now == cells[i][j].life:
					cells[i][j].active = True
					cells[i][j].now = 0
			else :
				if cells[i][j].now == 0 :
					spread.append((i,j))
				cells[i][j].now += 1
				if cells[i][j].now == cells[i][j].life:
					cells[i][j].dead = True

	spread.sort(key = lambda x : cells[x[0]][x[1]].life, reverse = True)
	for x,y in spread:
		for k in range(4):
			nx = x + dx[k]
			ny = y + dy[k]
			if cells[nx][ny] : continue
			cells[nx][ny] = cell(cells[x][y].life)


for test_case in range(T):
	ans = 0
	n,m,k = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(n)]
	cells = [[0] * 350 for _ in range(350)]
	for i in range(n):
		for j in range(m):
			if board[i][j] :
				cells[i+150][j+150] = cell(board[i][j])
	# N , M  <= 50 
	# K <= 300
	# K가 300이고 N,M이 50이면 최대 K/2만큼 번식하니까 
	# 배양 용기의 최대 크기는 350*350이다.

	for _ in range(k):
		simulate(cells)
	for i in range(350):
		for j in range(350):
			if cells[i][j] and not cells[i][j].dead:
				ans += 1
	print("#"+ str(test_case+1) + " " + str(ans))
