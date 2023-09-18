dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
board = [[-1]*n for _ in range(n)]
order = []
pref = [[] for _ in range((n**2) + 1)]
for x in [list(map(int, input().split())) for _ in range(n**2)] : 
    order.append(x[0])
    pref[x[0]] = x[1:]
    
# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
def setSeat():
    for o in order:
        # 초기 자리 설정 전부 다 빈칸이면 가장 왼쪽 위인 2,2에 앉힘
        if board[1][1] == -1 :
            board[1][1] = o
            continue
 
        # pref[o] : 현재 선택된 학생이 좋아하는 학생들의 번호
        # o : 현재 선택된 학생 번호
        # prefNum[i][j] : o가 좋아하는 학생이 몇명 앉아있는지
        nullNum = [[0] * n for _ in range(n)]
        prefNum = [[0] * n for _ in range(n)]
        maxPref = -1
        maxPrefidx = [-1,-1]

        for i in range(n):
            for j in range(n):
                if board[i][j] != -1 : continue
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if board[nx][ny] == -1 :
                            nullNum[i][j] += 1
                            continue
                        if board[nx][ny] in pref[o] :
                            prefNum[i][j] += 1
                
                if prefNum[i][j] > maxPref:
                    maxPref = prefNum[i][j]
                    maxPrefidx = [i,j]
                elif prefNum[i][j] == maxPref:
                    if nullNum[i][j] > nullNum[maxPrefidx[0]][maxPrefidx[1]]:
                        maxPrefidx = [i,j]
        # maxPref가 업데이트 안됐을 때 그대로 0,0에 업데이트 하는 경우 고쳐야함


        board[maxPrefidx[0]][maxPrefidx[1]] = o


def getScore() :
    scores = [0,1,10,100,1000]
    ans = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<n and 0<=ny < n :
                    if board[nx][ny] in pref[board[i][j]] :
                        cnt += 1
            ans += scores[cnt]
    return ans

setSeat()
#board = [[6,7,4],[8,5,2],[9,1,3]]
print(getScore())