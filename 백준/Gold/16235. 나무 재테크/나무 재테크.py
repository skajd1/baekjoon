def spring(): # 나무 성장
    for i in range(n):
        for j in range(n):
            for k, years in enumerate(trees[i][j]) :
                if years <= nour[i][j] :
                    nour[i][j] -= years
                    trees[i][j][k] += 1
                else : 
                    length = len(trees[i][j])
                    for _ in range(k,length):
                        dead[i][j].append(trees[i][j].pop())
                    break

def summer(): # 죽은 나무 양분 변화
    for i in range(n):
        for j in range(n):
            while dead[i][j]:
                nour[i][j] += (dead[i][j].pop() // 2)
    
def autumn(): #번식
    for i in range(n):
        for j in range(n):
            for tree in trees[i][j] :
                if tree % 5 == 0 :
                    for k in range(8):
                        nx = i + delta[k][0]
                        ny = j + delta[k][1]
                        if 0<=nx<n and 0<=ny<n :
                            trees[nx][ny].appendleft(1)

def winter(): # 양분 추가
    for i in range(n):
        for j in range(n):
            nour[i][j] += add[i][j]

from collections import deque
delta = [[-1,-1],[0,-1],[1,-1],[-1,1],[0,1],[1,1],[-1,0],[1,0]]
n,m,k = map(int, input().split())
nour = [[5] * n for _ in range(n)] # 초기 양분 5로 초기화
add = [list(map(int, input().split())) for _ in range(n)] # 겨울에 각 땅에 더해줄 양분 정보
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    for x,y,year in [map(int, input().split())] :
        trees[x-1][y-1].append(year)

for i in range(k) :
    spring()
    summer()
    autumn()
    winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])
print(ans)