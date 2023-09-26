# 0 1 2 3 왼 아래 오른 위
# A 0.1 0.1 0.07 0.07 0.01 0.01 0.05 0.02 0.02
delta = [
    [
        [1, -1],
        [-1, -1],
        [-1, 0],
        [1, 0],
        [-1, 1],
        [1, 1],
        [0, -2],
        [2, 0],
        [-2, 0],
    ],
    [
        [1, 1],
        [1, -1],
        [0, -1],
        [0, 1],
        [-1, -1],
        [-1, 1],
        [2, 0],
        [0, 2],
        [0, -2],
    ],
    [
        [-1, 1],
        [1, 1],
        [1, 0],
        [-1, 0],
        [1, -1],
        [-1, -1],
        [0, 2],
        [-2, 0],
        [2, 0],
    ],
    [
        [-1, -1],
        [-1, 1],
        [0, 1],
        [0, -1],
        [1, 1],
        [1, -1],
        [-2, 0],
        [0, -2],
        [0, 2],
    ],
]
alpha = [[0, -1], [1, 0], [0, 1], [-1, 0]]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

w = [
    0.1,
    0.1,
    0.07,
    0.07,
    0.01,
    0.01,
    0.05,
    0.02,
    0.02,
]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
tonado = [n // 2, n // 2]
dir = 0
ans = 0

cnt = 0
tmp = 0
d = 1

def moveTonado():
    global tonado, dir, cnt, d, tmp
    x, y = tonado
    nx = x + dx[dir]
    ny = y + dy[dir]
    tonado = [nx, ny]
    moveSand(dir)
    cnt += 1
    if cnt == d:
        dir = (dir + 1) % 4
        tmp += 1
        cnt = 0
        if tmp == 2:
            d += 1
            tmp = 0


def moveSand(ndir):
    global board, ans
    x, y = tonado
    sand = board[x][y]
    board[x][y] = 0
    tmp = 0
    for i, (dx, dy) in enumerate(delta[ndir]):
        nx, ny = x + dx, y + dy
        s = int(sand * w[i])
        tmp += s
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] += s
        else:
            ans += s
    nx, ny = x + alpha[ndir][0], y + alpha[ndir][1]
    if 0 <= nx < n and 0 <= ny < n:
        board[nx][ny] += sand - tmp
    else:
        ans += sand - tmp


while tonado != [0, -1]:
    moveTonado()
print(ans)