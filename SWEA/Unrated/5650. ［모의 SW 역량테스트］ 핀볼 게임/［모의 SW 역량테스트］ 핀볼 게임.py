from collections import defaultdict

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 0 오른쪽
# 1 아래
# 2 왼쪽
# 3 위

def getCount(x, y):
    maxCnt = 0
    # 해당 위치에서 시작하여 4방향 카운트하고 최대값 리턴하기
    for k in range(4):
        cnt = 0
        nowDirection = k
        prevX = x
        prevY = y
        while (1):
            nextX = prevX + dx[nowDirection]
            nextY = prevY + dy[nowDirection]

            if not chkRange(prevX, prevY) or (1 <= board[prevX][prevY] <= 5):
                cnt += 1

            # 벽에 부딫힐 때
            if not chkRange(nextX, nextY):
                maxCnt = max(cnt*2 + 1, maxCnt)
                break

            # 처음 위치로 돌아왔을 때 혹은 블랙홀 빠질 때
            elif board[nextX][nextY] == -1 or (nextX == x and nextY == y):
                maxCnt = max(cnt, maxCnt)
                break
            # 블록에 부딫힐 때
            elif 1 <= board[nextX][nextY] <= 5:
                blockNum = board[nextX][nextY]
                if blockNum == 1:
                    if nowDirection in [0, 3]:
                        nowDirection = (nowDirection + 2) % 4
                    else:
                        nowDirection = 0 if nowDirection == 1 else 3
                elif blockNum == 2:
                    if nowDirection in [0, 1]:
                        nowDirection = (nowDirection + 2) % 4
                    else:
                        nowDirection = 0 if nowDirection == 3 else 1
                elif blockNum == 3:
                    if nowDirection in [1, 2]:
                        nowDirection = (nowDirection + 2) % 4
                    else:
                        nowDirection = 1 if nowDirection == 0 else 2
                elif blockNum == 4:
                    if nowDirection in [2, 3]:
                        nowDirection = (nowDirection + 2) % 4
                    else:
                        nowDirection = 2 if nowDirection == 1 else 3
                else:
                    maxCnt = max(cnt * 2 + 1, maxCnt)
                    break

            # 웜홀에 빠질 때
            elif 6 <= board[nextX][nextY] <= 10:
                holeNum = board[nextX][nextY]
                for hx, hy in hole[holeNum]:
                    if nextX != hx or nextY != hy:
                        prevX = hx
                        prevY = hy
                continue

            # prevX prevY 업데이트
            prevX = nextX
            prevY = nextY

    return maxCnt


for t in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    chkRange = lambda x, y: True if 0 <= x < n and 0 <= y < n else False
    hole = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if 6 <= board[i][j] <= 10:
                hole[board[i][j]].append([i, j])

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0: continue
            cnt = getCount(i,j)
            if ans < cnt :
                ans = cnt


    print("#" + str(t) + " " + str(ans))
