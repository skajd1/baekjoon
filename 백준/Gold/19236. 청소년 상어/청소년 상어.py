# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# 1, 2, 3, 4, 5, 6, 7, 8
import copy
dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
fish = []
for _ in range(4):
	tmp = list(map(int, input().split()))
	fish.append(list(tmp[i:i + 2] for i in range(0, 8, 2)))

# -1은 상어 0은 빈칸
# 상어가 0,0 먹고 방향 가짐
answer = []
score = fish[0][0][0]
shark_pos = [0, 0]
shark_dir = fish[0][0][1]
fish[0][0] = [-1, shark_dir]


# 물고기 이동 함수
def moveOneFish(f, fish):
	global dir
	fish_copy = copy.deepcopy(fish)
		
	for i in range(4):
		for j in range(4):
			if fish_copy[i][j][0] == f:
				# 이동할 수 있을 때 까지 방향 전환
				cnt = 0
				while cnt < 8:
					cnt += 1
					dx, dy = dir[fish_copy[i][j][1]-1]
					# 범위, 상어 조건
					if (0 <= i + dx < 4 and 0 <= j + dy < 4 and fish_copy[i + dx][j + dy][0] != -1):
						# 이동 후 바로 return
						fish_copy[i][j], fish_copy[i + dx][j + dy] = fish_copy[i + dx][j + dy], fish_copy[i][j]
						return fish_copy
					else:
						# 1~8
						fish_copy[i][j][1] += 1
						fish_copy[i][j][1] %= 8
						
	# 물고기가 못움직이는 경우
	return fish_copy


def moveAllFish(fish):
	fish_copy = copy.deepcopy(fish)
	for i in range(1, 17):
		fish_copy = moveOneFish(i, fish_copy)
	return fish_copy

def available_shark(fish, shark_pos, shark_dir):
	global dir
	candidate_pos = []
	dx, dy = dir[shark_dir-1][0], dir[shark_dir-1][1]
	x, y = shark_pos[0], shark_pos[1]
	# 범위 내에 있으며, 빈칸이 아니면
	for i in range(1, 4):
		if 0 <= i * dx + x < 4 and 0 <= i * dy + y < 4 and fish[i * dx + x][
		  i * dy + y][0] != 0:
			candidate_pos.append([i * dx + x, i * dy + y])

	return candidate_pos


def dfs(cur_score, fish, sharkInfo):
	global answer
	# 물고기 이동
	fish = moveAllFish(fish)
	candidate_pos = available_shark(fish, sharkInfo[0], sharkInfo[1])
	
	if not candidate_pos:
		answer.append(cur_score)
		return 
	else:
		for x, y in candidate_pos:
			fish_copy = copy.deepcopy(fish)
			# 상어 이동
			
			new_sharkPos = [x, y]
			new_sharkDir = fish[x][y][1]
			fish_copy[sharkInfo[0][0]][sharkInfo[0][1]] = [0,0]
			fish_copy[x][y] = [-1, new_sharkDir]
			
			dfs(cur_score + fish[x][y][0] , fish_copy, [new_sharkPos, new_sharkDir])


dfs(score, fish, [shark_pos, shark_dir])
print(max(answer))
