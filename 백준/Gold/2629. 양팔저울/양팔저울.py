numChu = int(input())
chu = list(map(int, input().split()))
numGoo = int(input())
goo = list(map(int, input().split()))
answer = []

# 추를 사용해 만들 수 있는 무게들에 구슬 무게가 속해있는지 판별
# 이미 사용한 추는 사용 불가

candidate = set()
dp = [[0]*15001 for i in range(numChu+1)]

# 재귀 안쓰면 메모리 초과 난대
# for i in range(1,numChu+1):
#     w = chu[i-1]
#     tmp = []
#     for x,y in dp[i-1]:
#         tmp.append([w+x,y])
#         tmp.append([x,w+y])
#         tmp.append([x,y])
#     dp.append(tmp)

# for arr in dp:
#     for x,y in arr :
#         candidate.add(abs(x-y))

def dfs(chu,cur,left,right):
    global candidate
    global dp
    new = abs(left-right)
    if new not in candidate:
        candidate.add(new)
    if cur == len(chu):
        return 0
    if dp[cur][new] == 0 :
        dfs(chu,cur+1,left+chu[cur],right)
        dfs(chu,cur+1,left,right+chu[cur])
        dfs(chu,cur+1,left,right)
        dp[cur][new] = 1

dfs(chu,0,0,0)

for x in goo:
    if x in candidate :
        answer.append("Y")
    else :
        answer.append("N")
print(*answer)