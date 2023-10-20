class Horse:
	def __init__(self, x, y, d, num):
		self.x = x
		self.y = y
		self.d = d
		self.num = num
	def move(self,x,y):
		self.x = x
		self.y = y
	def change(self):
		if self.d == 0 or self.d == 2 :
			self.d += 1
		else :
			self.d -= 1
n,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
stack = [[[] for _ in range(n)] for _ in range(n)]
# 0 1 2 3
# 오 왼 위 아래
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horses = []
for i in range(k):
	x,y,d = map(int, input().split())
	horses.append(Horse(x-1,y-1,d-1,i))
	stack[x-1][y-1].append(i)


turn = 0
while True :
	turn += 1
	find = False
	if turn > 1000 :
		turn = -1
		break
	for horse in horses :
		nx = horse.x + dx[horse.d]
		ny = horse.y + dy[horse.d]
		if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2 :
			horse.change()
			nx = horse.x + dx[horse.d]
			ny = horse.y + dy[horse.d]
			if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2 :
				continue
		hs = []
		for i, h in enumerate(stack[horse.x][horse.y]):
			if h == horse.num :
				hs.extend(stack[horse.x][horse.y][i:])
				stack[horse.x][horse.y] = stack[horse.x][horse.y][:i]
				break
		# 빨간색
		if board[nx][ny] == 1:
			hs.reverse()
		for h in hs :
			horses[h].move(nx,ny)
			stack[nx][ny].append(h)
		
		if len(stack[nx][ny]) >= 4 :
			find = True
			break
	if find :
		break
print(turn)