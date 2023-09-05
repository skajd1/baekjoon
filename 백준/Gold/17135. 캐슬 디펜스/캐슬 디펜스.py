import sys
from collections import deque
from itertools import combinations

n, m, D = map(int,sys.stdin.readline().rstrip().split())
board = []
for i in range(n) :
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    board.append(line)
combi = list(combinations([i for i in range(m)],3))
dx = [0,-1,0]
dy = [-1,0,1]
def search(anchor) :
    arr = [x[:] for x in board]
    visited = [[0] * m for _ in range(n)]
    # que = deque()
    cnt = 0
    for i in range(n-1,-1,-1) :
        temp = []
        for arrow in anchor :
            que = deque([(i,arrow,1)])
            while que :
                x,y,d = que.popleft()
                if arr[x][y] == 1 :
                    temp.append([x,y])
                    if visited[x][y] == 0 :
                        visited[x][y] = 1
                        cnt += 1
                    break

                if d < D :
                    for j in range(3) :
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if 0 <= nx < n and 0 <= ny < m :
                            que.append((nx,ny,d+1))
        for tx,ty in temp :
            arr[tx][ty] = 0
    return cnt
answer = 0
for anchor in combi :
    answer = max(answer,search(anchor))
print(answer)