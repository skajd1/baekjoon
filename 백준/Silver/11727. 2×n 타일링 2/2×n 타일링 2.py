n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]
# 0 세로 1 가로 2 가로세로
# dp[i]는 i번째 타일을 채웠을 때의 경우의 수
dp[1][0] = 1
if n == 1 :
    print(1)
    exit(0)
dp[2][0] = 1
dp[2][1] = 1
dp[2][2] = 1
for i in range(3, n + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
    dp[i][1] = dp[i - 2][0] + dp[i - 2][1] + dp[i - 2][2]
    dp[i][2] = dp[i - 2][0] + dp[i - 2][1] + dp[i - 2][2]
print(sum(dp[n]) % 10007)