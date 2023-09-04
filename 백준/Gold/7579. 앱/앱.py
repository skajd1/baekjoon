# dp[i] : i 메모리를 비활성화 할 때 최소 비용
# 혹은 dp[i] : i 비용으로 활성화 할 수 있는 최대 메모리
# memory_cost를 c,m 순으로 정렬 후 
# dp[i] 가 M보다 커지는 최초의 i가 정답
n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
memory_cost = []
for me,c in zip(memory,cost):
    memory_cost.append((me,c))
memory_cost.sort(key=lambda x: (x[1],x[0]))
dp = [0] * (sum(cost)+1)
for me,c in memory_cost:
    for i in range(sum(cost),c-1,-1):
        dp[i] = max(dp[i],dp[i-c]+me)
for i in range(sum(cost)+1):
    if dp[i] >= m:
        print(i)
        break